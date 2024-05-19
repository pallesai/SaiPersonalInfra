#!/usr/bin/env node
import { SaiPersonalInfraStack } from '../lib/sai_personal_infra-stack';
import {App} from "aws-cdk-lib";

const app = new App();
new SaiPersonalInfraStack(app, 'SaiPersonalInfraStack');
