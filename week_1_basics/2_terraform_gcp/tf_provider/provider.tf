provider "oci" {
  tenancy_ocid     = "ocid1.tenancy.oc1..aaaaaaaakhi4bb5gntjf3ksdfclyfcrhw3jyahpoimsuwgruacrsebmla3da"
  user_ocid        = "ocid1.user.oc1..aaaaaaaaiaj2hsgxddikluwiaxcnfmh66swh67admtd3zf34u5qbenpn2e3q"
  #fingerprint      = "your-fingerprint" if it doesn't work come here and add this one
  #private_key_path = "path/to/your/private-key.pem" like the above
  region           = "eu-frankfurt-1"
}