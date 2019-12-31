
Currently CDK hasn't supported lambda application autoscaling, use cli instead

aws application-autoscaling register-scalable-target \
    --service-namespace lambda \
    --scalable-dimension lambda:function:ProvisionedConcurrency \
    --resource-id function:with-provisioned-concurre-BackendWithProvisionedCo-1O0WDZFYOX1TX:latest \
    --min-capacity 0 \
    --max-capacity 800
    

aws application-autoscaling put-scaling-policy --service-namespace lambda \
--scalable-dimension lambda:function:ProvisionedConcurrency \
--resource-id function:with-provisioned-concurre-BackendWithProvisionedCo-1O0WDZFYOX1TX:latest \
--policy-name my-policy --policy-type TargetTrackingScaling \
--target-tracking-scaling-policy-configuration '{ "TargetValue": 0.7, "PredefinedMetricSpecification": { "PredefinedMetricType": "LambdaProvisionedConcurrencyUtilization" }}'
