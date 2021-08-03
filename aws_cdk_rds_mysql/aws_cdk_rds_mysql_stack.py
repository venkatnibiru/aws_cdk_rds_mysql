from aws_cdk import(
core as cdk,
aws_rds as rds,
aws_ec2 as ec2
)
from aws_cdk_rds_mysql.myvars import *

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class RdsStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # VPC creation
        workload_vpc = ec2.Vpc(self, 'default_vpc', cidr= VPC_CIDR)

        # RDS Provisioning Section
        rds_sql= rds.DatabaseInstance(
            self, "RDS",
            database_name=DB_NAME,
            engine=rds.DatabaseInstanceEngine.mysql(
                version=rds.MysqlEngineVersion.VER_8_0_16
            ),
            vpc=workload_vpc,
            port=DB_PORT,
            instance_type= ec2.InstanceType.of(
                ec2.InstanceClass.MEMORY4,
                ec2.InstanceSize.LARGE,
            ),
            removal_policy=core.RemovalPolicy.DESTROY,
            deletion_protection=False
        )