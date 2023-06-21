# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ErrorResponse]
    :ivar additional_info: The error additional info.
    :vartype additional_info:
     list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorResponse]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class PolicyExemption(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """The policy exemption.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.resource.policy.v2022_07_01_preview.models.SystemData
    :ivar id: The ID of the policy exemption.
    :vartype id: str
    :ivar name: The name of the policy exemption.
    :vartype name: str
    :ivar type: The type of the resource (Microsoft.Authorization/policyExemptions).
    :vartype type: str
    :ivar policy_assignment_id: The ID of the policy assignment that is being exempted. Required.
    :vartype policy_assignment_id: str
    :ivar policy_definition_reference_ids: The policy definition reference ID list when the
     associated policy assignment is an assignment of a policy set definition.
    :vartype policy_definition_reference_ids: list[str]
    :ivar exemption_category: The policy exemption category. Possible values are Waiver and
     Mitigated. Required. Known values are: "Waiver" and "Mitigated".
    :vartype exemption_category: str or
     ~azure.mgmt.resource.policy.v2022_07_01_preview.models.ExemptionCategory
    :ivar expires_on: The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ) of
     the policy exemption.
    :vartype expires_on: ~datetime.datetime
    :ivar display_name: The display name of the policy exemption.
    :vartype display_name: str
    :ivar description: The description of the policy exemption.
    :vartype description: str
    :ivar metadata: The policy exemption metadata. Metadata is an open ended object and is
     typically a collection of key value pairs.
    :vartype metadata: JSON
    :ivar resource_selectors: The resource selector list to filter policies by resource properties.
    :vartype resource_selectors:
     list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ResourceSelector]
    :ivar assignment_scope_validation: The option whether validate the exemption is at or under the
     assignment scope. Known values are: "Default" and "DoNotValidate".
    :vartype assignment_scope_validation: str or
     ~azure.mgmt.resource.policy.v2022_07_01_preview.models.AssignmentScopeValidation
    """

    _validation = {
        "system_data": {"readonly": True},
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "policy_assignment_id": {"required": True},
        "exemption_category": {"required": True},
    }

    _attribute_map = {
        "system_data": {"key": "systemData", "type": "SystemData"},
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "policy_assignment_id": {"key": "properties.policyAssignmentId", "type": "str"},
        "policy_definition_reference_ids": {"key": "properties.policyDefinitionReferenceIds", "type": "[str]"},
        "exemption_category": {"key": "properties.exemptionCategory", "type": "str"},
        "expires_on": {"key": "properties.expiresOn", "type": "iso-8601"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "description": {"key": "properties.description", "type": "str"},
        "metadata": {"key": "properties.metadata", "type": "object"},
        "resource_selectors": {"key": "properties.resourceSelectors", "type": "[ResourceSelector]"},
        "assignment_scope_validation": {"key": "properties.assignmentScopeValidation", "type": "str"},
    }

    def __init__(
        self,
        *,
        policy_assignment_id: str,
        exemption_category: Union[str, "_models.ExemptionCategory"],
        policy_definition_reference_ids: Optional[List[str]] = None,
        expires_on: Optional[datetime.datetime] = None,
        display_name: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[JSON] = None,
        resource_selectors: Optional[List["_models.ResourceSelector"]] = None,
        assignment_scope_validation: Optional[Union[str, "_models.AssignmentScopeValidation"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword policy_assignment_id: The ID of the policy assignment that is being exempted.
         Required.
        :paramtype policy_assignment_id: str
        :keyword policy_definition_reference_ids: The policy definition reference ID list when the
         associated policy assignment is an assignment of a policy set definition.
        :paramtype policy_definition_reference_ids: list[str]
        :keyword exemption_category: The policy exemption category. Possible values are Waiver and
         Mitigated. Required. Known values are: "Waiver" and "Mitigated".
        :paramtype exemption_category: str or
         ~azure.mgmt.resource.policy.v2022_07_01_preview.models.ExemptionCategory
        :keyword expires_on: The expiration date and time (in UTC ISO 8601 format yyyy-MM-ddTHH:mm:ssZ)
         of the policy exemption.
        :paramtype expires_on: ~datetime.datetime
        :keyword display_name: The display name of the policy exemption.
        :paramtype display_name: str
        :keyword description: The description of the policy exemption.
        :paramtype description: str
        :keyword metadata: The policy exemption metadata. Metadata is an open ended object and is
         typically a collection of key value pairs.
        :paramtype metadata: JSON
        :keyword resource_selectors: The resource selector list to filter policies by resource
         properties.
        :paramtype resource_selectors:
         list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ResourceSelector]
        :keyword assignment_scope_validation: The option whether validate the exemption is at or under
         the assignment scope. Known values are: "Default" and "DoNotValidate".
        :paramtype assignment_scope_validation: str or
         ~azure.mgmt.resource.policy.v2022_07_01_preview.models.AssignmentScopeValidation
        """
        super().__init__(**kwargs)
        self.system_data = None
        self.id = None
        self.name = None
        self.type = None
        self.policy_assignment_id = policy_assignment_id
        self.policy_definition_reference_ids = policy_definition_reference_ids
        self.exemption_category = exemption_category
        self.expires_on = expires_on
        self.display_name = display_name
        self.description = description
        self.metadata = metadata
        self.resource_selectors = resource_selectors
        self.assignment_scope_validation = assignment_scope_validation


class PolicyExemptionListResult(_serialization.Model):
    """List of policy exemptions.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: An array of policy exemptions.
    :vartype value: list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.PolicyExemption]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[PolicyExemption]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: Optional[List["_models.PolicyExemption"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: An array of policy exemptions.
        :paramtype value: list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.PolicyExemption]
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = None


class PolicyExemptionUpdate(_serialization.Model):
    """The policy exemption for Patch request.

    :ivar resource_selectors: The resource selector list to filter policies by resource properties.
    :vartype resource_selectors:
     list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ResourceSelector]
    :ivar assignment_scope_validation: The option whether validate the exemption is at or under the
     assignment scope. Known values are: "Default" and "DoNotValidate".
    :vartype assignment_scope_validation: str or
     ~azure.mgmt.resource.policy.v2022_07_01_preview.models.AssignmentScopeValidation
    """

    _attribute_map = {
        "resource_selectors": {"key": "properties.resourceSelectors", "type": "[ResourceSelector]"},
        "assignment_scope_validation": {"key": "properties.assignmentScopeValidation", "type": "str"},
    }

    def __init__(
        self,
        *,
        resource_selectors: Optional[List["_models.ResourceSelector"]] = None,
        assignment_scope_validation: Optional[Union[str, "_models.AssignmentScopeValidation"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword resource_selectors: The resource selector list to filter policies by resource
         properties.
        :paramtype resource_selectors:
         list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.ResourceSelector]
        :keyword assignment_scope_validation: The option whether validate the exemption is at or under
         the assignment scope. Known values are: "Default" and "DoNotValidate".
        :paramtype assignment_scope_validation: str or
         ~azure.mgmt.resource.policy.v2022_07_01_preview.models.AssignmentScopeValidation
        """
        super().__init__(**kwargs)
        self.resource_selectors = resource_selectors
        self.assignment_scope_validation = assignment_scope_validation


class ResourceSelector(_serialization.Model):
    """The resource selector to filter policies by resource properties.

    :ivar name: The name of the resource selector.
    :vartype name: str
    :ivar selectors: The list of the selector expressions.
    :vartype selectors: list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.Selector]
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "selectors": {"key": "selectors", "type": "[Selector]"},
    }

    def __init__(
        self, *, name: Optional[str] = None, selectors: Optional[List["_models.Selector"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword name: The name of the resource selector.
        :paramtype name: str
        :keyword selectors: The list of the selector expressions.
        :paramtype selectors: list[~azure.mgmt.resource.policy.v2022_07_01_preview.models.Selector]
        """
        super().__init__(**kwargs)
        self.name = name
        self.selectors = selectors


class Selector(_serialization.Model):
    """The selector expression.

    :ivar kind: The selector kind. Known values are: "resourceLocation", "resourceType",
     "resourceWithoutLocation", and "policyDefinitionReferenceId".
    :vartype kind: str or ~azure.mgmt.resource.policy.v2022_07_01_preview.models.SelectorKind
    :ivar in_property: The list of values to filter in.
    :vartype in_property: list[str]
    :ivar not_in: The list of values to filter out.
    :vartype not_in: list[str]
    """

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "in_property": {"key": "in", "type": "[str]"},
        "not_in": {"key": "notIn", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        kind: Optional[Union[str, "_models.SelectorKind"]] = None,
        in_property: Optional[List[str]] = None,
        not_in: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword kind: The selector kind. Known values are: "resourceLocation", "resourceType",
         "resourceWithoutLocation", and "policyDefinitionReferenceId".
        :paramtype kind: str or ~azure.mgmt.resource.policy.v2022_07_01_preview.models.SelectorKind
        :keyword in_property: The list of values to filter in.
        :paramtype in_property: list[str]
        :keyword not_in: The list of values to filter out.
        :paramtype not_in: list[str]
        """
        super().__init__(**kwargs)
        self.kind = kind
        self.in_property = in_property
        self.not_in = not_in


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or
     ~azure.mgmt.resource.policy.v2022_07_01_preview.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or
     ~azure.mgmt.resource.policy.v2022_07_01_preview.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or
         ~azure.mgmt.resource.policy.v2022_07_01_preview.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or
         ~azure.mgmt.resource.policy.v2022_07_01_preview.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at