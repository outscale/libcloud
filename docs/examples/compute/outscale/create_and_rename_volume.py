from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

key = 'my_key'
secret = 'my_secret'
region = 'eu-west-2'
service = 'api'

name = "name"

Driver = get_driver(Provider.OUTSCALE)
driver = Driver(key=key, secret=secret, region=region, service=service)

volume = driver.create_volume(ex_subregion_name=region)

driver.create_tag(resource_id=volume.id, tag_key="Name", tag_value=name)

volume = driver.list_volumes(volume_ids=[volume.id])[0]

print(volume)