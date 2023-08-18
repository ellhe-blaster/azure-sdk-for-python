# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._configuration_assignments_for_resource_group_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConfigurationAssignmentsForResourceGroupOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.maintenance.aio.MaintenanceManagementClient`'s
        :attr:`configuration_assignments_for_resource_group` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, configuration_assignment_name: str, **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Get configuration assignment.

        Get configuration assignment for resource..

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ConfigurationAssignment] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            configuration_assignment_name=configuration_assignment_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConfigurationAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: _models.ConfigurationAssignment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Required.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Required.
        :type configuration_assignment: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: Union[_models.ConfigurationAssignment, IO],
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Is either a
         ConfigurationAssignment type or a IO type. Required.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigurationAssignment] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(configuration_assignment, (IOBase, bytes)):
            _content = configuration_assignment
        else:
            _json = self._serialize.body(configuration_assignment, "ConfigurationAssignment")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            configuration_assignment_name=configuration_assignment_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ConfigurationAssignment", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ConfigurationAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}"
    }

    @overload
    async def update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: _models.ConfigurationAssignment,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Required.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Required.
        :type configuration_assignment: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        configuration_assignment_name: str,
        configuration_assignment: Union[_models.ConfigurationAssignment, IO],
        **kwargs: Any
    ) -> _models.ConfigurationAssignment:
        """Create configuration assignment.

        Register configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Configuration assignment name. Required.
        :type configuration_assignment_name: str
        :param configuration_assignment: The configurationAssignment. Is either a
         ConfigurationAssignment type or a IO type. Required.
        :type configuration_assignment: ~azure.mgmt.maintenance.models.ConfigurationAssignment or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfigurationAssignment] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(configuration_assignment, (IOBase, bytes)):
            _content = configuration_assignment
        else:
            _json = self._serialize.body(configuration_assignment, "ConfigurationAssignment")

        request = build_update_request(
            resource_group_name=resource_group_name,
            configuration_assignment_name=configuration_assignment_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ConfigurationAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}"
    }

    @distributed_trace_async
    async def delete(
        self, resource_group_name: str, configuration_assignment_name: str, **kwargs: Any
    ) -> Optional[_models.ConfigurationAssignment]:
        """Unregister configuration for resource.

        Unregister configuration for resource.

        :param resource_group_name: Resource group name. Required.
        :type resource_group_name: str
        :param configuration_assignment_name: Unique configuration assignment name. Required.
        :type configuration_assignment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ConfigurationAssignment or None or the result of cls(response)
        :rtype: ~azure.mgmt.maintenance.models.ConfigurationAssignment or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[Optional[_models.ConfigurationAssignment]] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            configuration_assignment_name=configuration_assignment_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.MaintenanceError, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("ConfigurationAssignment", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Maintenance/configurationAssignments/{configurationAssignmentName}"
    }