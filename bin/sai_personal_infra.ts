#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { SaiPersonalInfraStack } from '../lib/sai_personal_infra-stack';

const app = new cdk.App();
new SaiPersonalInfraStack(app, 'SaiPersonalInfraStack');
