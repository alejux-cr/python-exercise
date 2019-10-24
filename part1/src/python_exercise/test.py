ordereddict(
    [
        ('DjangoEC2Instance', 
        ordereddict(
            [
                ('Type', 'AWS::EC2::Instance'), 
                ('Properties', 
                ordereddict(
                    [
                        ('ImageId', ['AWSRegionArch2AMI', <ruamel.yaml.comments.TaggedScalar object at 0x0000021E62CBCC18>, ['AWSInstanceType2Arch', <ruamel.yaml.comments.TaggedScalar object at 0x0000021E62CBCBE0>, 'Arch']]), ('KeyName', <ruamel.yaml.comments.TaggedScalar object at 0x0000021E62CBCBA8>), ('InstanceType', <ruamel.yaml.comments.TaggedScalar object at 0x0000021E62CBCCC0>), ('SecurityGroups', [<ruamel.yaml.comments.TaggedScalar object at 0x0000021E62CBCC50>]), ('BlockDeviceMappings', [ordereddict([('DeviceName', '/dev/sda1'), ('Ebs', ordereddict([('VolumeSize', 50)]))]), ordereddict([('DeviceName', '/dev/sdm'), ('Ebs', ordereddict([('VolumeSize', 100)]))])])]))]))])