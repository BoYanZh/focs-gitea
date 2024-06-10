# coding: utf-8

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import focs_gitea
from focs_gitea.api.user_api import UserApi  # noqa: E501
from focs_gitea.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = focs_gitea.api.user_api.UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_current_user_repo(self):
        """Test case for create_current_user_repo

        Create a repository  # noqa: E501
        """
        pass

    def test_create_user_variable(self):
        """Test case for create_user_variable

        Create a user-level variable  # noqa: E501
        """
        pass

    def test_delete_user_secret(self):
        """Test case for delete_user_secret

        Delete a secret in a user scope  # noqa: E501
        """
        pass

    def test_delete_user_variable(self):
        """Test case for delete_user_variable

        Delete a user-level variable which is created by current doer  # noqa: E501
        """
        pass

    def test_get_user_settings(self):
        """Test case for get_user_settings

        Get user settings  # noqa: E501
        """
        pass

    def test_get_user_variable(self):
        """Test case for get_user_variable

        Get a user-level variable which is created by current doer  # noqa: E501
        """
        pass

    def test_get_user_variables_list(self):
        """Test case for get_user_variables_list

        Get the user-level list of variables which is created by current doer  # noqa: E501
        """
        pass

    def test_get_verification_token(self):
        """Test case for get_verification_token

        Get a Token to verify  # noqa: E501
        """
        pass

    def test_update_user_secret(self):
        """Test case for update_user_secret

        Create or Update a secret value in a user scope  # noqa: E501
        """
        pass

    def test_update_user_settings(self):
        """Test case for update_user_settings

        Update user settings  # noqa: E501
        """
        pass

    def test_update_user_variable(self):
        """Test case for update_user_variable

        Update a user-level variable which is created by current doer  # noqa: E501
        """
        pass

    def test_user_add_email(self):
        """Test case for user_add_email

        Add email addresses  # noqa: E501
        """
        pass

    def test_user_block_user(self):
        """Test case for user_block_user

        Block a user  # noqa: E501
        """
        pass

    def test_user_check_following(self):
        """Test case for user_check_following

        Check if one user is following another user  # noqa: E501
        """
        pass

    def test_user_check_user_block(self):
        """Test case for user_check_user_block

        Check if a user is blocked by the authenticated user  # noqa: E501
        """
        pass

    def test_user_create_hook(self):
        """Test case for user_create_hook

        Create a hook  # noqa: E501
        """
        pass

    def test_user_create_o_auth2_application(self):
        """Test case for user_create_o_auth2_application

        creates a new OAuth2 application  # noqa: E501
        """
        pass

    def test_user_create_token(self):
        """Test case for user_create_token

        Create an access token  # noqa: E501
        """
        pass

    def test_user_current_check_following(self):
        """Test case for user_current_check_following

        Check whether a user is followed by the authenticated user  # noqa: E501
        """
        pass

    def test_user_current_check_starring(self):
        """Test case for user_current_check_starring

        Whether the authenticated is starring the repo  # noqa: E501
        """
        pass

    def test_user_current_delete_follow(self):
        """Test case for user_current_delete_follow

        Unfollow a user  # noqa: E501
        """
        pass

    def test_user_current_delete_gpg_key(self):
        """Test case for user_current_delete_gpg_key

        Remove a GPG key  # noqa: E501
        """
        pass

    def test_user_current_delete_key(self):
        """Test case for user_current_delete_key

        Delete a public key  # noqa: E501
        """
        pass

    def test_user_current_delete_star(self):
        """Test case for user_current_delete_star

        Unstar the given repo  # noqa: E501
        """
        pass

    def test_user_current_get_gpg_key(self):
        """Test case for user_current_get_gpg_key

        Get a GPG key  # noqa: E501
        """
        pass

    def test_user_current_get_key(self):
        """Test case for user_current_get_key

        Get a public key  # noqa: E501
        """
        pass

    def test_user_current_list_followers(self):
        """Test case for user_current_list_followers

        List the authenticated user's followers  # noqa: E501
        """
        pass

    def test_user_current_list_following(self):
        """Test case for user_current_list_following

        List the users that the authenticated user is following  # noqa: E501
        """
        pass

    def test_user_current_list_gpg_keys(self):
        """Test case for user_current_list_gpg_keys

        List the authenticated user's GPG keys  # noqa: E501
        """
        pass

    def test_user_current_list_keys(self):
        """Test case for user_current_list_keys

        List the authenticated user's public keys  # noqa: E501
        """
        pass

    def test_user_current_list_repos(self):
        """Test case for user_current_list_repos

        List the repos that the authenticated user owns  # noqa: E501
        """
        pass

    def test_user_current_list_starred(self):
        """Test case for user_current_list_starred

        The repos that the authenticated user has starred  # noqa: E501
        """
        pass

    def test_user_current_list_subscriptions(self):
        """Test case for user_current_list_subscriptions

        List repositories watched by the authenticated user  # noqa: E501
        """
        pass

    def test_user_current_post_gpg_key(self):
        """Test case for user_current_post_gpg_key

        Create a GPG key  # noqa: E501
        """
        pass

    def test_user_current_post_key(self):
        """Test case for user_current_post_key

        Create a public key  # noqa: E501
        """
        pass

    def test_user_current_put_follow(self):
        """Test case for user_current_put_follow

        Follow a user  # noqa: E501
        """
        pass

    def test_user_current_put_star(self):
        """Test case for user_current_put_star

        Star the given repo  # noqa: E501
        """
        pass

    def test_user_current_tracked_times(self):
        """Test case for user_current_tracked_times

        List the current user's tracked times  # noqa: E501
        """
        pass

    def test_user_delete_access_token(self):
        """Test case for user_delete_access_token

        delete an access token  # noqa: E501
        """
        pass

    def test_user_delete_avatar(self):
        """Test case for user_delete_avatar

        Delete Avatar  # noqa: E501
        """
        pass

    def test_user_delete_email(self):
        """Test case for user_delete_email

        Delete email addresses  # noqa: E501
        """
        pass

    def test_user_delete_hook(self):
        """Test case for user_delete_hook

        Delete a hook  # noqa: E501
        """
        pass

    def test_user_delete_o_auth2_application(self):
        """Test case for user_delete_o_auth2_application

        delete an OAuth2 Application  # noqa: E501
        """
        pass

    def test_user_edit_hook(self):
        """Test case for user_edit_hook

        Update a hook  # noqa: E501
        """
        pass

    def test_user_get(self):
        """Test case for user_get

        Get a user  # noqa: E501
        """
        pass

    def test_user_get_current(self):
        """Test case for user_get_current

        Get the authenticated user  # noqa: E501
        """
        pass

    def test_user_get_heatmap_data(self):
        """Test case for user_get_heatmap_data

        Get a user's heatmap  # noqa: E501
        """
        pass

    def test_user_get_hook(self):
        """Test case for user_get_hook

        Get a hook  # noqa: E501
        """
        pass

    def test_user_get_o_auth2_application(self):
        """Test case for user_get_o_auth2_application

        get an OAuth2 Application  # noqa: E501
        """
        pass

    def test_user_get_oauth2_application(self):
        """Test case for user_get_oauth2_application

        List the authenticated user's oauth2 applications  # noqa: E501
        """
        pass

    def test_user_get_runner_registration_token(self):
        """Test case for user_get_runner_registration_token

        Get an user's actions runner registration token  # noqa: E501
        """
        pass

    def test_user_get_stop_watches(self):
        """Test case for user_get_stop_watches

        Get list of all existing stopwatches  # noqa: E501
        """
        pass

    def test_user_get_tokens(self):
        """Test case for user_get_tokens

        List the authenticated user's access tokens  # noqa: E501
        """
        pass

    def test_user_list_activity_feeds(self):
        """Test case for user_list_activity_feeds

        List a user's activity feeds  # noqa: E501
        """
        pass

    def test_user_list_blocks(self):
        """Test case for user_list_blocks

        List users blocked by the authenticated user  # noqa: E501
        """
        pass

    def test_user_list_emails(self):
        """Test case for user_list_emails

        List the authenticated user's email addresses  # noqa: E501
        """
        pass

    def test_user_list_followers(self):
        """Test case for user_list_followers

        List the given user's followers  # noqa: E501
        """
        pass

    def test_user_list_following(self):
        """Test case for user_list_following

        List the users that the given user is following  # noqa: E501
        """
        pass

    def test_user_list_gpg_keys(self):
        """Test case for user_list_gpg_keys

        List the given user's GPG keys  # noqa: E501
        """
        pass

    def test_user_list_hooks(self):
        """Test case for user_list_hooks

        List the authenticated user's webhooks  # noqa: E501
        """
        pass

    def test_user_list_keys(self):
        """Test case for user_list_keys

        List the given user's public keys  # noqa: E501
        """
        pass

    def test_user_list_repos(self):
        """Test case for user_list_repos

        List the repos owned by the given user  # noqa: E501
        """
        pass

    def test_user_list_starred(self):
        """Test case for user_list_starred

        The repos that the given user has starred  # noqa: E501
        """
        pass

    def test_user_list_subscriptions(self):
        """Test case for user_list_subscriptions

        List the repositories watched by a user  # noqa: E501
        """
        pass

    def test_user_list_teams(self):
        """Test case for user_list_teams

        List all the teams a user belongs to  # noqa: E501
        """
        pass

    def test_user_search(self):
        """Test case for user_search

        Search for users  # noqa: E501
        """
        pass

    def test_user_unblock_user(self):
        """Test case for user_unblock_user

        Unblock a user  # noqa: E501
        """
        pass

    def test_user_update_avatar(self):
        """Test case for user_update_avatar

        Update Avatar  # noqa: E501
        """
        pass

    def test_user_update_o_auth2_application(self):
        """Test case for user_update_o_auth2_application

        update an OAuth2 Application, this includes regenerating the client secret  # noqa: E501
        """
        pass

    def test_user_verify_gpg_key(self):
        """Test case for user_verify_gpg_key

        Verify a GPG key  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
