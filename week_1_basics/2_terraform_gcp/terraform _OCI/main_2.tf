#Chatgpt version:
# terraform {
#   required_version = ">= 1.0"
#   backend "local" {}  # Can change from "local" to another backend, depending on your preferences
#   required_providers {
#     oci = {
#       source  = "hashicorp/oci"
#       version = "~> 5.0"  # Use an appropriate OCI provider version
#     }
#   }
# }

#https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/tf-provider/01-summary.htm
provider "oci" {
  tenancy_ocid     = "ocid1.tenancy.oc1..aaaaaaaakhi4bb5gntjf3ksdfclyfcrhw3jyahpoimsuwgruacrsebmla3da"
  user_ocid        = "ocid1.user.oc1..aaaaaaaaiaj2hsgxddikluwiaxcnfmh66swh67admtd3zf34u5qbenpn2e3q"
  #fingerprint      = "your-fingerprint" if it doesn't work come here and add this one
  #private_key_path = "path/to/your/private-key.pem" like the above
  region           = "eu-frankfurt-1"
}

resource "oci_objectstorage_bucket" "test_bucket" {
    #Required
    compartment_id = var.compartment_id
    name = var.bucket_name
    namespace = var.bucket_namespace

    #Optional
    access_type = var.bucket_access_type
    auto_tiering = var.bucket_auto_tiering
    defined_tags = {"Operations.CostCenter"= "42"}
    freeform_tags = {"Department"= "Finance"}
    kms_key_id = oci_kms_key.test_key.id
    metadata = var.bucket_metadata
    object_events_enabled = var.bucket_object_events_enabled
    storage_tier = var.bucket_storage_tier
    retention_rules {
        display_name = var.retention_rule_display_name
        duration {
            #Required
            time_amount = var.retention_rule_duration_time_amount
            time_unit = var.retention_rule_duration_time_unit
        }
        time_rule_locked = var.retention_rule_time_rule_locked
    }
    versioning = var.bucket_versioning
}

