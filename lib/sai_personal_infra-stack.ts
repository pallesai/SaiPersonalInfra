import {aws_lambda as lambda, Duration, Stack, StackProps} from 'aws-cdk-lib';
import {Construct} from "constructs";
import {Code, LayerVersion, Runtime} from "aws-cdk-lib/aws-lambda";
import * as path from 'path';

export class SaiPersonalInfraStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const Lambda = new lambda.Function(this, "ICBCLambdaStack", {
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: "main.handler",
      code: lambda.Code.fromAsset("lambda"),
      memorySize: 1024,
      timeout: Duration.seconds(10),
      layers: [this.createLambdaLayer()]
    });
  }

  private createLambdaLayer() : LayerVersion {
    return new LayerVersion(this, 'LambdaDependenciesLayer', {
       code: Code.fromAsset(path.join(__dirname, '../layer')),
       compatibleRuntimes: [Runtime.PYTHON_3_8],
       license: 'Apache-2.0',
       description: 'A layer containing dependencies for the ICBC lambda',
     });
  }
}
