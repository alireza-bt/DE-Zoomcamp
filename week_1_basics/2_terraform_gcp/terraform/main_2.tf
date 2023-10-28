# maybe just create a dataset and data storage thing??
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
provider "oci" {
  tenancy_ocid     = "your-tenancy-ocid"
  user_ocid        = "your-user-ocid"
  fingerprint      = "your-fingerprint"
  private_key_path = "path/to/your/private-key.pem"
  region           = "your-oci-region"
}

resource "oci_database_autonomous_data_warehouse" "example_adw" {
  compartment_id      = "your-compartment-id"
  db_name             = "exampledb"
  cpu_core_count      = 1
  data_storage_size   = 1
  display_name        = "example-adw"
  admin_password      = "YourStrongPassword1!"
  tde_wallet_password = "YourStrongPassword1!"
}

resource "oci_database_autonomous_data_warehouse_table" "example_table" {
  autonomous_data_warehouse_id = oci_database_autonomous_data_warehouse.example_adw.id
  table_name                   = "example_table"
  column {
    name     = "column1"
    data_type = "VARCHAR2"
    char_length = 50
  }
  column {
    name     = "column2"
    data_type = "NUMBER"
  }
}
