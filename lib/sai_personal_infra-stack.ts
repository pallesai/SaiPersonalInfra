import { Stack, StackProps, aws_lambda as lambda } from 'aws-cdk-lib';
import {Construct} from "constructs";

export class SaiPersonalInfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const Lambda = new lambda.Function(this, "ICBCLambdaStack", {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: "main.handler",
      code: lambda.Code.fromAsset("lambda"),
      memorySize: 1024,
    });
  }
}
