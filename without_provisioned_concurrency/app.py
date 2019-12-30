#!/usr/bin/env python3

from aws_cdk import core

from without_provisioned_concurrency.without_provisioned_concurrency_stack import WithoutProvisionedConcurrencyStack


app = core.App()
WithoutProvisionedConcurrencyStack(app, "without-provisioned-concurrency", env={'region': 'ap-southeast-1'})
app.synth()
