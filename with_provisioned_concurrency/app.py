#!/usr/bin/env python3

from aws_cdk import core

from with_provisioned_concurrency.with_provisioned_concurrency_stack import WithProvisionedConcurrencyStack


app = core.App()
WithProvisionedConcurrencyStack(app, "with-provisioned-concurrency")

app.synth()
