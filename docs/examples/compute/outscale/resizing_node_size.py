from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

key = 'my_key'
secret = 'my_secret'
region = 'eu-west-2'
service = 'api'

node_id = "node_id"
size = 100

Driver = get_driver(Provider.OUTSCALE)
driver = Driver(key=key, secret=secret, region=region, service=service)

node = driver.list_nodes(tag_keys=["Ids"], tag_values=[node_id])[0]
volume = driver.list_volumes(link_volume_ids=[node.id])[0]

new_snapshot = driver.create_volume_snapshot(volume=volume)
new_volume = driver.create_volume(size, snapshot=new_snapshot)

driver.detach_volume(volume)
driver.attach_volume(node, new_volume, "device_name")

node = driver.list_nodes(tag_keys=["Ids"], tag_values=[node_id])[0]

print(node)