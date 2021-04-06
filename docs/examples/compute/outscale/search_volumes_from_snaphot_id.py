from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

key = 'my_key'
secret = 'my_secret'
region = 'eu-west-2'
service = 'api'

snapshot_id = "snapshot_id"

Driver = get_driver(Provider.OUTSCALE)
driver = Driver(key=key, secret=secret, region=region, service=service)

nodes = driver.list_volumes(snapshot_ids=[snapshot_id])

print(nodes)
