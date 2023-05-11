# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.confidentialledger import ConfidentialLedger

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-confidentialledger
# USAGE
    python managed_ccf_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ConfidentialLedger(
        credential=DefaultAzureCredential(),
        subscription_id="0000000-0000-0000-0000-000000000001",
    )

    response = client.managed_ccf.list_by_resource_group(
        resource_group_name="DummyResourceGroupName",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/confidentialledger/resource-manager/Microsoft.ConfidentialLedger/preview/2023-01-26-preview/examples/ManagedCCF_List.json
if __name__ == "__main__":
    main()