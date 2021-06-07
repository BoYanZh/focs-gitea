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


class TrackedTime(object):
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
        'created': 'datetime',
        'id': 'int',
        'issue': 'Issue',
        'issue_id': 'int',
        'time': 'int',
        'user_id': 'int',
        'user_name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'issue': 'issue',
        'issue_id': 'issue_id',
        'time': 'time',
        'user_id': 'user_id',
        'user_name': 'user_name'
    }

    def __init__(self, created=None, id=None, issue=None, issue_id=None, time=None, user_id=None, user_name=None, _configuration=None):  # noqa: E501
        """TrackedTime - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._id = None
        self._issue = None
        self._issue_id = None
        self._time = None
        self._user_id = None
        self._user_name = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if issue is not None:
            self.issue = issue
        if issue_id is not None:
            self.issue_id = issue_id
        if time is not None:
            self.time = time
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name

    @property
    def created(self):
        """Gets the created of this TrackedTime.  # noqa: E501


        :return: The created of this TrackedTime.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this TrackedTime.


        :param created: The created of this TrackedTime.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this TrackedTime.  # noqa: E501


        :return: The id of this TrackedTime.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrackedTime.


        :param id: The id of this TrackedTime.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def issue(self):
        """Gets the issue of this TrackedTime.  # noqa: E501


        :return: The issue of this TrackedTime.  # noqa: E501
        :rtype: Issue
        """
        return self._issue

    @issue.setter
    def issue(self, issue):
        """Sets the issue of this TrackedTime.


        :param issue: The issue of this TrackedTime.  # noqa: E501
        :type: Issue
        """

        self._issue = issue

    @property
    def issue_id(self):
        """Gets the issue_id of this TrackedTime.  # noqa: E501

        deprecated (only for backwards compatibility)  # noqa: E501

        :return: The issue_id of this TrackedTime.  # noqa: E501
        :rtype: int
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        """Sets the issue_id of this TrackedTime.

        deprecated (only for backwards compatibility)  # noqa: E501

        :param issue_id: The issue_id of this TrackedTime.  # noqa: E501
        :type: int
        """

        self._issue_id = issue_id

    @property
    def time(self):
        """Gets the time of this TrackedTime.  # noqa: E501

        Time in seconds  # noqa: E501

        :return: The time of this TrackedTime.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TrackedTime.

        Time in seconds  # noqa: E501

        :param time: The time of this TrackedTime.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def user_id(self):
        """Gets the user_id of this TrackedTime.  # noqa: E501

        deprecated (only for backwards compatibility)  # noqa: E501

        :return: The user_id of this TrackedTime.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TrackedTime.

        deprecated (only for backwards compatibility)  # noqa: E501

        :param user_id: The user_id of this TrackedTime.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this TrackedTime.  # noqa: E501


        :return: The user_name of this TrackedTime.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TrackedTime.


        :param user_name: The user_name of this TrackedTime.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(TrackedTime, dict):
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
        if not isinstance(other, TrackedTime):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrackedTime):
            return True

        return self.to_dict() != other.to_dict()
