import json
from extent_table import ExtentTable
from table_maker import TableMaker

Volumes = [
    {
        "AvailabilityZone": "us-east-1a",
        "Attachments": [
            {
                "AttachTime": "2013-12-18T22:35:00.000Z",
                "InstanceId": "i-1234567890abcdef0",
                "VolumeId": "vol-049df61146c4d7901",
                "State": "attached",
                "DeleteOnTermination": "true",
                "Device": "/dev/sda1"
            }
        ],
        "Tags": [
            {
                "Value": "DBJanitor-Private",
                "Key": "Name"
            },
            {
                "Value": "DBJanitor",
                "Key": "Owner"
            },
            {
                "Value": "Database",
                "Key": "Product"
            },
            {
                "Value": "DB Janitor",
                "Key": "Portfolio"
            },
            {
                "Value": "DB Service",
                "Key": "Service"
            }
        ],
        "VolumeType": "standard",
        "VolumeId": "vol-049df61146c4d7901",
        "State": "in-use",
        "SnapshotId": "snap-1234567890abcdef0",
        "CreateTime": "2013-12-18T22:35:00.084Z",
        "Size": 8
    },
    {
        "AvailabilityZone": "us-east-1a",
        "Attachments": [],
        "VolumeType": "io1",
        "VolumeId": "vol-1234567890abcdef0",
        "State": "available",
        "Iops": 1000,
        "SnapshotId": "null",
        "CreateTime": "2014-02-27T00:02:41.791Z",
        "Size": 100
    }
]

volumes = json.dumps(Volumes)
volumes = json.loads(volumes)

extent_table = ExtentTable()
table_maker = TableMaker(extent_table)
table_maker.convert_json_objects_to_tables(volumes, "volumes")
table_maker.show_tables(8)
table_maker.save_tables("./", export_as="html")
