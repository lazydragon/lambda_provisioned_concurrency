from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class WithoutProvisionedConcurrencyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        backend = _lambda.Function(
            self, 'BackendWithoutProvisionedConcurrencyHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.asset('lambda'),
            handler='backend.handler',
            tracing=_lambda.Tracing.ACTIVE,
        )
        
        apigw.LambdaRestApi(
            self, 'WithoutProvisionedConcurrency',
            handler=backend,
            deploy_options={
                "tracing_enabled": True,
            },
        )

