# coding: utf-8

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.14.2+makersmelx+BoYanZh
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from focs_gitea.configuration import Configuration


class Team(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_create_org_repo': 'bool',
        'description': 'str',
        'id': 'int',
        'includes_all_repositories': 'bool',
        'name': 'str',
        'organization': 'Organization',
        'permission': 'str',
        'units': 'list[str]'
    }

    attribute_map = {
        'can_create_org_repo': 'can_create_org_repo',
        'description': 'description',
        'id': 'id',
        'includes_all_repositories': 'includes_all_repositories',
        'name': 'name',
        'organization': 'organization',
        'permission': 'permission',
        'units': 'units'
    }

    def __init__(self, can_create_org_repo=None, description=None, id=None, includes_all_repositories=None, name=None, organization=None, permission=None, units=None, _configuration=None):  # noqa: E501
        """Team - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._can_create_org_repo = None
        self._description = None
        self._id = None
        self._includes_all_repositories = None
        self._name = None
        self._organization = None
        self._permission = None
        self._units = None
        self.discriminator = None

        if can_create_org_repo is not None:
            self.can_create_org_repo = can_create_org_repo
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if includes_all_repositories is not None:
            self.includes_all_repositories = includes_all_repositories
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if permission is not None:
            self.permission = permission
        if units is not None:
            self.units = units

    @property
    def can_create_org_repo(self):
        """Gets the can_create_org_repo of this Team.  # noqa: E501


        :return: The can_create_org_repo of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_org_repo

    @can_create_org_repo.setter
    def can_create_org_repo(self, can_create_org_repo):
        """Sets the can_create_org_repo of this Team.


        :param can_create_org_repo: The can_create_org_repo of this Team.  # noqa: E501
        :type: bool
        """

        self._can_create_org_repo = can_create_org_repo

    @property
    def description(self):
        """Gets the description of this Team.  # noqa: E501


        :return: The description of this Team.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Team.


        :param description: The description of this Team.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501


        :return: The id of this Team.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.


        :param id: The id of this Team.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def includes_all_repositories(self):
        """Gets the includes_all_repositories of this Team.  # noqa: E501


        :return: The includes_all_repositories of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._includes_all_repositories

    @includes_all_repositories.setter
    def includes_all_repositories(self, includes_all_repositories):
        """Sets the includes_all_repositories of this Team.


        :param includes_all_repositories: The includes_all_repositories of this Team.  # noqa: E501
        :type: bool
        """

        self._includes_all_repositories = includes_all_repositories

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501


        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this Team.  # noqa: E501


        :return: The organization of this Team.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Team.


        :param organization: The organization of this Team.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def permission(self):
        """Gets the permission of this Team.  # noqa: E501


        :return: The permission of this Team.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this Team.


        :param permission: The permission of this Team.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "read", "write", "admin", "owner"]  # noqa: E501
        if (self._configuration.client_side_validation and
                permission not in allowed_values):
            raise ValueError(
                "Invalid value for `permission` ({0}), must be one of {1}"  # noqa: E501
                .format(permission, allowed_values)
            )

        self._permission = permission

    @property
    def units(self):
        """Gets the units of this Team.  # noqa: E501


        :return: The units of this Team.  # noqa: E501
        :rtype: list[str]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this Team.


        :param units: The units of this Team.  # noqa: E501
        :type: list[str]
        """

        self._units = units

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Team, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Team):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Team):
            return True

        return self.to_dict() != other.to_dict()
