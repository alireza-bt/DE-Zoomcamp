I wanted to test Terraform in OCI based on the following tutorial:
https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/tf-provider/01-summary.htm

# Test is done using the OCI shell, so some steps could be skipped!
# The next experiment could be doing the same using the OCI-VM instance

### 1-Prepare
1. installing the OCI supported version of terraform (I installed 1.2.9)
    - I also used the tfenv to manage tf versions (https://github.com/tfutils/tfenv)
2. Create RSA Keys (skipped, because of OCI shell)
3. Add list policies (skipped, ...)
4. Gathering required info such as tenancy-id, etc. from the OCI console.

------------
### 2-Create Scripts
All the scripts should be in the same directory

1. Add API Key-based auth. (provider.tf)
2. Add a Data Source (availability-domains.tf)
3. Add outputs, which fetches a list ADs (outputs.tf)

------------
### 3-Run Scripts
1. terraform init
2. terraform plan
3. terraform apply