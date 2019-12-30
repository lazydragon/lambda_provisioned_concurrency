import time

from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class WithProvisionedConcurrencyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        backend = _lambda.Function(
            self, 'BackendWithProvisionedConcurrencyHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='backend.handler',
            tracing=_lambda.Tracing.ACTIVE,
        )
        
        latest_version = backend.add_version(str(time.time()))
        alias = _lambda.Alias(self, 'Latest', alias_name='latest', version=latest_version)
        
        apigw.LambdaRestApi(
            self, 'WithProvisionedConcurrency',
            handler=alias,
            deploy_options={
                "tracing_enabled": True,
            },
        )

