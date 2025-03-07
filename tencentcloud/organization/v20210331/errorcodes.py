# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Operation failed.
FAILEDOPERATION = 'FailedOperation'

# The account has been registered.
FAILEDOPERATION_ACCOUNTALREADYREGISTER = 'FailedOperation.AccountAlreadyRegister'

# The application already exists.
FAILEDOPERATION_APPLYEXIST = 'FailedOperation.ApplyExist'

# The user has not completed identity verification.
FAILEDOPERATION_AUTHINFOEMPTY = 'FailedOperation.AuthInfoEmpty'

# Enterprise real name mismatch.
FAILEDOPERATION_AUTHINFONOTSAME = 'FailedOperation.AuthInfoNotSame'

# The user has not completed enterprise identity verification.
FAILEDOPERATION_AUTHNOTENTERPRISE = 'FailedOperation.AuthNotEnterprise'

# The mailbox binding link has expired.
FAILEDOPERATION_BINDEMAILLINKEXPIRED = 'FailedOperation.BindEmailLinkExpired'

# The mailbox binding link is invalid.
FAILEDOPERATION_BINDEMAILLINKINVALID = 'FailedOperation.BindEmailLinkInvalid'

# Member permission change record exists.
FAILEDOPERATION_CHANGEPERMISSIONRECORDEXIST = 'FailedOperation.ChangePermissionRecordExist'

# Failed to check the mobile phone binding capacity limit.
FAILEDOPERATION_CHECKACCOUNTPHONEBINDLIMIT = 'FailedOperation.CheckAccountPhoneBindLimit'

# Failed to check the mailbox binding status.
FAILEDOPERATION_CHECKMAILACCOUNT = 'FailedOperation.CheckMailAccount'

# Permission configurations created for a directory exceed the upper limit.
FAILEDOPERATION_CONFIGURATIONOVERUPPERLIMIT = 'FailedOperation.ConfigurationOverUpperLimit'

# An exception occurred while creating the member.
FAILEDOPERATION_CREATEACCOUNT = 'FailedOperation.CreateAccount'

# Failed to create the billing permission
FAILEDOPERATION_CREATEBILLINGPERMISSIONERR = 'FailedOperation.CreateBillingPermissionErr'

# The number of times of account identity verification exceeds the upper limit.
FAILEDOPERATION_CREATEMEMBERAUTHOVERLIMIT = 'FailedOperation.CreateMemberAuthOverLimit'

# Failed to create the policy
FAILEDOPERATION_CREATEPOLICY = 'FailedOperation.CreatePolicy'

# Created successfully.
FAILEDOPERATION_CREATERECORDALREADYSUCCESS = 'FailedOperation.CreateRecordAlreadySuccess'

# The creation record does not exist.
FAILEDOPERATION_CREATERECORDNOTEXIST = 'FailedOperation.CreateRecordNotExist'

# An exception occurred while creating the role.
FAILEDOPERATION_CREATEROLE = 'FailedOperation.CreateRole'

# Custom policies bound to the permission configuration exceed the upper limit.
FAILEDOPERATION_CUSTOMPOLICYOVERUPPERLIMIT = 'FailedOperation.CustomPolicyOverUpperLimit'

# SQL execution error.
FAILEDOPERATION_DBOPERATIONERROR = 'FailedOperation.DBOperationError'

# Metadata document decoding failed.
FAILEDOPERATION_DECODEMETADATADOCUMENTFAILED = 'FailedOperation.DecodeMetadataDocumentFailed'

# The user group still contains users and does not allow deleting users.
FAILEDOPERATION_DELETEGROUPNOTALLOWEXISTUSER = 'FailedOperation.DeleteGroupNotAllowExistUser'

# Exception occurred when deleting the authorization policy.
FAILEDOPERATION_DELETEPOLICY = 'FailedOperation.DeletePolicy'

# An error occurred in the query of the organization service usage status.
FAILEDOPERATION_DESCRIBEORGSERVICEUSAGESTATUSERR = 'FailedOperation.DescribeOrgServiceUsageStatusErr'

# You cannot quit an organization created by yourself.
FAILEDOPERATION_DISABLEQUITSELFCREATEDORGANIZATION = 'FailedOperation.DisableQuitSelfCreatedOrganization'

# The email has been used.
FAILEDOPERATION_EMAILALREADYUSED = 'FailedOperation.EmailAlreadyUsed'

# Mailbox binding has become invalid.
FAILEDOPERATION_EMAILBINDRECORDINVALID = 'FailedOperation.EmailBindRecordInvalid'

# There are shared resources with other organization members or from other organization members.
FAILEDOPERATION_EXISTOTHERORGANIZATIONMEMBERSHARED = 'FailedOperation.ExistOtherOrganizationMemberShared'

# There are shared members not in the organization.
FAILEDOPERATION_EXISTSHAREMEMBERNOTINORGANIZATION = 'FailedOperation.ExistShareMemberNotInOrganization'

# Errors occurred when account's regional attributes are obtained.
FAILEDOPERATION_GETACCOUNTREGION = 'FailedOperation.GetAccountRegion'

# An error occurred while querying the identity information.
FAILEDOPERATION_GETAUTHINFO = 'FailedOperation.GetAuthInfo'

# Failed to query the policy.
FAILEDOPERATION_GETPOLICYDETAIL = 'FailedOperation.GetPolicyDetail'

# User groups created exceed the upper limit.
FAILEDOPERATION_GROUPOVERUPPERLIMIT = 'FailedOperation.GroupOverUpperLimit'

# User group type and user type do not match.
FAILEDOPERATION_GROUPTYPEUSERTYPENOTMATCH = 'FailedOperation.GroupTypeUserTypeNotMatch'

# Members of the CIC user group exceed the limit.
FAILEDOPERATION_GROUPUSERCOUNTOVERUPPERLIMIT = 'FailedOperation.GroupUserCountOverUpperLimit'

# The shared unit has different shared resource types.
FAILEDOPERATION_HASDIFFERENTRESOURCETYPE = 'FailedOperation.HasDifferentResourceType'

# The CIC service has been activated.
FAILEDOPERATION_IDENTITYCENTERALREADYOPEN = 'FailedOperation.IdentityCenterAlreadyOpen'

# The user has not performed identity verification and cannot activate the CIC service.
FAILEDOPERATION_IDENTITYCENTERNOTAUTH = 'FailedOperation.IdentityCenterNotAuth'

# The user has not performed enterprise identity verification and cannot activate the CIC service.
FAILEDOPERATION_IDENTITYCENTERNOTENTERPRISEAUTH = 'FailedOperation.IdentityCenterNotEnterpriseAuth'

# The CIC service is not enabled.
FAILEDOPERATION_IDENTITYCENTERNOTOPEN = 'FailedOperation.IdentityCenterNotOpen'

# The user is not an admin of the Tencent Cloud Organization and cannot activate the CIC service.
FAILEDOPERATION_IDENTITYCENTERNOTORGANIZATIONMANAGER = 'FailedOperation.IdentityCenterNotOrganizationManager'

# The user has not activated Tencent Cloud Organization and cannot activate the CIC service.
FAILEDOPERATION_IDENTITYCENTERORGANIZATIONNOTOPEN = 'FailedOperation.IdentityCenterOrganizationNotOpen'

# The uploaded file is invalid.
FAILEDOPERATION_IMPORTFILEILLEGAL = 'FailedOperation.ImportFileIllegal'

# The invitation already exists.
FAILEDOPERATION_INVITATIONEXIST = 'FailedOperation.InvitationExist'

# Manually created user groups cannot be deleted.
FAILEDOPERATION_MANUALGROUPNOTDELETE = 'FailedOperation.ManualGroupNotDelete'

# Manually created user groups cannot be updated.
FAILEDOPERATION_MANUALGROUPNOTUPDATE = 'FailedOperation.ManualGroupNotUpdate'

# Manually created users cannot be deleted.
FAILEDOPERATION_MANUALUSERNOTDELETE = 'FailedOperation.ManualUserNotDelete'

# Manually created users cannot be updated.
FAILEDOPERATION_MANUALUSERNOTUPDATE = 'FailedOperation.ManualUserNotUpdate'

# Mailbox binding failed.
FAILEDOPERATION_MEMBERBINDEMAILERROR = 'FailedOperation.MemberBindEmailError'

# Verification mobile numbe binding failed.
FAILEDOPERATION_MEMBERBINDPHONEERROR = 'FailedOperation.MemberBindPhoneError'

# The member has a mailbox.
FAILEDOPERATION_MEMBEREMAILEXIST = 'FailedOperation.MemberEmailExist'

# The member has a payer and cannot be deleted.
FAILEDOPERATION_MEMBEREXISTDELEGATEPAYERNOTALLOWDELETE = 'FailedOperation.MemberExistDelegatePayerNotAllowDelete'

# The member already belongs to another organization.
FAILEDOPERATION_MEMBEREXISTINOTHERORGANIZATION = 'FailedOperation.MemberExistInOtherOrganization'

# Member authorization is in use.
FAILEDOPERATION_MEMBERIDENTITYAUTHUSED = 'FailedOperation.MemberIdentityAuthUsed'

# The member is a payer and cannot be deleted.
FAILEDOPERATION_MEMBERISDELEGATEPAYERNOTALLOWDELETE = 'FailedOperation.MemberIsDelegatePayerNotAllowDelete'

# The name is already in use.
FAILEDOPERATION_MEMBERNAMEUSED = 'FailedOperation.MemberNameUsed'

# The member authorization policy name is already in use.
FAILEDOPERATION_MEMBERPOLICYNAMEEXIST = 'FailedOperation.MemberPolicyNameExist'

# The member is sharing resources and cannot quit the organization.
FAILEDOPERATION_MEMBERSHARERESOURCE = 'FailedOperation.MemberShareResource'

# IdP metadata parsing failed.
FAILEDOPERATION_METADATACOSPARSINGFAILED = 'FailedOperation.MetadataCosParsingFailed'

# There are members in this department
FAILEDOPERATION_NODENOTEMPTY = 'FailedOperation.NodeNotEmpty'

# You can only invite accounts within the same site.
FAILEDOPERATION_NOTSAMEREGION = 'FailedOperation.NotSameRegion'

# An error occurred while manipulating the billing member permission.
FAILEDOPERATION_OPERATEBILLINGPERMISSIONERR = 'FailedOperation.OperateBillingPermissionErr'

# Failed to manipulate the policy.
FAILEDOPERATION_OPERATEPOLICY = 'FailedOperation.OperatePolicy'

# The member is an entity admin account and cannot quit the organization.
FAILEDOPERATION_ORGANIZATIONAUTHMANAGENOTALLOWDELETE = 'FailedOperation.OrganizationAuthManageNotAllowDelete'

# Real-name authentication relationship already exists.
FAILEDOPERATION_ORGANIZATIONAUTHRELATIONEXIST = 'FailedOperation.OrganizationAuthRelationExist'

# The organization already exists.
FAILEDOPERATION_ORGANIZATIONEXISTALREADY = 'FailedOperation.OrganizationExistAlready'

# Organization identity is in use.
FAILEDOPERATION_ORGANIZATIONIDENTITYINUSED = 'FailedOperation.OrganizationIdentityInUsed'

# Organization identity name is in use.
FAILEDOPERATION_ORGANIZATIONIDENTITYNAMEUSED = 'FailedOperation.OrganizationIdentityNameUsed'

# Organization identity policy is invalid.
FAILEDOPERATION_ORGANIZATIONIDENTITYPOLICYERROR = 'FailedOperation.OrganizationIdentityPolicyError'

# Member already exists.
FAILEDOPERATION_ORGANIZATIONMEMBEREXIST = 'FailedOperation.OrganizationMemberExist'

# The member name already exists.
FAILEDOPERATION_ORGANIZATIONMEMBERNAMEUSED = 'FailedOperation.OrganizationMemberNameUsed'

# The member account does not exist.
FAILEDOPERATION_ORGANIZATIONMEMBERNOTEXIST = 'FailedOperation.OrganizationMemberNotExist'

# The number of nodes to be deleted exceeds the upper limit.
FAILEDOPERATION_ORGANIZATIONNODEDELETEOVERLIMIT = 'FailedOperation.OrganizationNodeDeleteOverLimit'

# The node name is already in use.
FAILEDOPERATION_ORGANIZATIONNODENAMEUSED = 'FailedOperation.OrganizationNodeNameUsed'

# There are nodes in the organization.
FAILEDOPERATION_ORGANIZATIONNODENOTEMPTY = 'FailedOperation.OrganizationNodeNotEmpty'

# The organization node does not exist.
FAILEDOPERATION_ORGANIZATIONNODENOTEXIST = 'FailedOperation.OrganizationNodeNotExist'

# There are members in this organization.
FAILEDOPERATION_ORGANIZATIONNOTEMPTY = 'FailedOperation.OrganizationNotEmpty'

# The organization permission is invalid.
FAILEDOPERATION_ORGANIZATIONPERMISSIONILLEGAL = 'FailedOperation.OrganizationPermissionIllegal'

# The organization policy is invalid.
FAILEDOPERATION_ORGANIZATIONPOLICYILLEGAL = 'FailedOperation.OrganizationPolicyIllegal'

# Group policy is not disabled.
FAILEDOPERATION_ORGANIZATIONPOLICYISNOTDISABLED = 'FailedOperation.OrganizationPolicyIsNotDisabled'

# Organization service delegation is in use.
FAILEDOPERATION_ORGANIZATIONSERVICEASSIGNISUSE = 'FailedOperation.OrganizationServiceAssignIsUse'

# Distribution system calling error.
FAILEDOPERATION_PARTNERMANAGEMENTERR = 'FailedOperation.PartnerManagementErr'

# The payer is invalid.
FAILEDOPERATION_PAYUINILLEGAL = 'FailedOperation.PayUinIllegal'

# Failed to exit the shared unit.
FAILEDOPERATION_QUITSHAREUINT = 'FailedOperation.QuitShareUint'

# Failed to leave the shared unit.
FAILEDOPERATION_QUITSHAREUINTERROR = 'FailedOperation.QuitShareUintError'

# Failed to exit the shared unit.
FAILEDOPERATION_QUITESHAREUNIT = 'FailedOperation.QuiteShareUnit'

# The invitation has already been sent before.
FAILEDOPERATION_RESENTINVITATION = 'FailedOperation.ReSentInvitation'

# Resources exceed the maximum upper limit.
FAILEDOPERATION_RESOURCEOVERLIMIT = 'FailedOperation.ResourceOverLimit'

# The permission authorization already exists.
FAILEDOPERATION_ROLECONFIGURATIONAUTHORIZATIONALREADYEXIST = 'FailedOperation.RoleConfigurationAuthorizationAlreadyExist'

# The permission configuration authorization exists.
FAILEDOPERATION_ROLECONFIGURATIONAUTHORIZATIONEXIST = 'FailedOperation.RoleConfigurationAuthorizationExist'

# The number of permission configuration authorizations exceeds the limit.
FAILEDOPERATION_ROLECONFIGURATIONAUTHORIZATIONOVERLIMIT = 'FailedOperation.RoleConfigurationAuthorizationOverLimit'

# The access configuration has been deployed to member accounts.
FAILEDOPERATION_ROLECONFIGURATIONPROVISIONINGALREADYDEPLOYED = 'FailedOperation.RoleConfigurationProvisioningAlreadyDeployed'

# The permission configuration synchronization has a status error.
FAILEDOPERATION_ROLECONFIGURATIONPROVISIONINGSTATUSERROR = 'FailedOperation.RoleConfigurationProvisioningStatusError'

# SAML metadata document acquisition failed.
FAILEDOPERATION_SAMLMETADATADOCUMENTGETFAILED = 'FailedOperation.SAMLMetadataDocumentGetFailed'

# SAML service provider creation failed.
FAILEDOPERATION_SAMLSERVICEPROVIDERCREATEFAILED = 'FailedOperation.SAMLServiceProviderCreateFailed'

# The SAML identity provider information cannot be cleared when SSO is enabled.
FAILEDOPERATION_SSOSTATUSENABLENOTCLEARIDENTITYPROVIDER = 'FailedOperation.SSoStatusEnableNotClearIdentityProvider'

# Failed to generate the SCIM key.
FAILEDOPERATION_SCIMCREDENTIALGENERATEERROR = 'FailedOperation.ScimCredentialGenerateError'

# The shared region does not exist.
FAILEDOPERATION_SHAREAREANOTEXIST = 'FailedOperation.ShareAreaNotExist'

# The shared member does not exist.
FAILEDOPERATION_SHAREMEMBERNOTEXIST = 'FailedOperation.ShareMemberNotExist'

# The member is using a shared resource.
FAILEDOPERATION_SHARERESOURCEMEMBERINUSE = 'FailedOperation.ShareResourceMemberInUse'

# The shared resource does not exist.
FAILEDOPERATION_SHARERESOURCENOTEXIST = 'FailedOperation.ShareResourceNotExist'

# The shared resource type does not exist.
FAILEDOPERATION_SHARERESOURCETYPENOTEXIST = 'FailedOperation.ShareResourceTypeNotExist'

# Shared unit is not empty.
FAILEDOPERATION_SHAREUNITNOTEMPTY = 'FailedOperation.ShareUnitNotEmpty'

# The shared unit does not exist.
FAILEDOPERATION_SHAREUNITNOTEXIST = 'FailedOperation.ShareUnitNotExist'

# The UIN does not belong to the organization.
FAILEDOPERATION_SOMEUINSNOTINORGANIZATION = 'FailedOperation.SomeUinsNotInOrganization'

# The sub-account has an identity.
FAILEDOPERATION_SUBACCOUNTIDENTITYEXIST = 'FailedOperation.SubAccountIdentityExist'

# The sub-account does not exist.
FAILEDOPERATION_SUBACCOUNTNOTEXIST = 'FailedOperation.SubAccountNotExist'

# The synchronized user group does not allow adding users.
FAILEDOPERATION_SYNCHRONIZEDGROUPNOTADDUSER = 'FailedOperation.SynchronizedGroupNotAddUser'

# The synchronized user groups cannot be deleted.
FAILEDOPERATION_SYNCHRONIZEDGROUPNOTDELETE = 'FailedOperation.SynchronizedGroupNotDelete'

# The synchronized user group does not allow deleting users.
FAILEDOPERATION_SYNCHRONIZEDGROUPNOTREMOVEUSER = 'FailedOperation.SynchronizedGroupNotRemoveUser'

# The synchronized user group cannot be updated.
FAILEDOPERATION_SYNCHRONIZEDGROUPNOTUPDATE = 'FailedOperation.SynchronizedGroupNotUpdate'

# The synchronized user cannot be deleted.
FAILEDOPERATION_SYNCHRONIZEDUSERNOTDELETE = 'FailedOperation.SynchronizedUserNotDelete'

# The synchronized user cannot be modified.
FAILEDOPERATION_SYNCHRONIZEDUSERNOTUPDATE = 'FailedOperation.SynchronizedUserNotUpdate'

# System policies bound to the permission configuration exceed the upper limit.
FAILEDOPERATION_SYSTEMPOLICYOVERUPPERLIMIT = 'FailedOperation.SystemPolicyOverUpperLimit'

# Tagging error.
FAILEDOPERATION_TAGRESOURCESERROR = 'FailedOperation.TagResourcesError'

# Data file uploading failed.
FAILEDOPERATION_UPLOADMETADATAFAILED = 'FailedOperation.UploadMetadataFailed'

# Users joining the user group exceed the limit.
FAILEDOPERATION_USERADDGROUPCOUNTOVERUPPERLIMIT = 'FailedOperation.UserAddGroupCountOverUpperLimit'

# Users created exceed the upper limit.
FAILEDOPERATION_USEROVERUPPERLIMIT = 'FailedOperation.UserOverUpperLimit'

# The user synchronization already exists.
FAILEDOPERATION_USERPROVISIONINGALREADYEXISTS = 'FailedOperation.UserProvisioningAlreadyExists'

# The user synchronization exists.
FAILEDOPERATION_USERPROVISIONINGEXISTS = 'FailedOperation.UserProvisioningExists'

# The user synchronization failed.
FAILEDOPERATION_USERPROVISIONINGFAILED = 'FailedOperation.UserProvisioningFailed'

# The number of synchronized users exceeds the limit.
FAILEDOPERATION_USERPROVISIONINGOVERLIMIT = 'FailedOperation.UserProvisioningOverLimit'

# The X509 certificate already exists.
FAILEDOPERATION_X509CERTIFICATEALREADYEXIST = 'FailedOperation.X509CertificateAlreadyExist'

# X509 certificate parsing failed.
FAILEDOPERATION_X509CERTIFICATEPARSINGFAILED = 'FailedOperation.X509CertificateParsingFailed'

# XML parsing for the metadata document failed.
FAILEDOPERATION_XMLDATAUNMARSHALFAILED = 'FailedOperation.XMLDataUnmarshalFailed'

# The user zoneId of the CIC service does not exist.
FAILEDOPERATION_ZONEIDNOTEXIST = 'FailedOperation.ZoneIdNotExist'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The member in pay-on-behalf mode is not allowed to exit the organization voluntarily.
INVALIDPARAMETER_ALLOWQUITILLEGAL = 'InvalidParameter.AllowQuitIllegal'

# The permission configuration cannot be bound to this policy.
INVALIDPARAMETER_BINDPOLICYNAMENOTALLOWED = 'InvalidParameter.BindPolicyNameNotAllowed'

# Incorrect mobile phone verification code.
INVALIDPARAMETER_CODEERROR = 'InvalidParameter.CodeError'

# The mobile phone verification code has expired.
INVALIDPARAMETER_CODEEXPIRED = 'InvalidParameter.CodeExpired'

# The permission configuration name already exists.
INVALIDPARAMETER_CONFIGURATIONNAMEALREADYEXISTS = 'InvalidParameter.ConfigurationNameAlreadyExists'

# The permission configuration name has a format error.
INVALIDPARAMETER_CONFIGURATIONNAMEFORMATERROR = 'InvalidParameter.ConfigurationNameFormatError'

# The email address already exists.
INVALIDPARAMETER_EMAILALREADYEXISTS = 'InvalidParameter.EmailAlreadyExists'

# The user group name already exists.
INVALIDPARAMETER_GROUPNAMEALREADYEXISTS = 'InvalidParameter.GroupNameAlreadyExists'

# The user group name has a format error.
INVALIDPARAMETER_GROUPNAMEFORMATERROR = 'InvalidParameter.GroupNameFormatError'

# The user group does not exist.
INVALIDPARAMETER_GROUPNOTEXIST = 'InvalidParameter.GroupNotExist'

# The user already exists in the user group.
INVALIDPARAMETER_GROUPUSERALREADYEXISTS = 'InvalidParameter.GroupUserAlreadyExists'

# The user does not exist in the user group.
INVALIDPARAMETER_GROUPUSERNOTEXIST = 'InvalidParameter.GroupUserNotExist'

# The mailbox is invalid.
INVALIDPARAMETER_INVALIDEMAIL = 'InvalidParameter.InvalidEmail'

# Invalid nextToken.
INVALIDPARAMETER_NEXTTOKENINVALID = 'InvalidParameter.NextTokenInvalid'

# The organization member does not exist.
INVALIDPARAMETER_ORGANIZATIONMEMBERNOTEXIST = 'InvalidParameter.OrganizationMemberNotExist'

# The organization node does not exist.
INVALIDPARAMETER_ORGANIZATIONNODENOTEXIST = 'InvalidParameter.OrganizationNodeNotExist'

# Parameter error.
INVALIDPARAMETER_PARAMERROR = 'InvalidParameter.ParamError'

# The password is invalid.
INVALIDPARAMETER_PASSWORDILLEGAL = 'InvalidParameter.PasswordIllegal'

# The custom policy content cannot be empty.
INVALIDPARAMETER_POLICYDOCUMENTEMPTY = 'InvalidParameter.PolicyDocumentEmpty'

# The policy name already exists.
INVALIDPARAMETER_POLICYNAMEALREADYEXISTS = 'InvalidParameter.PolicyNameAlreadyExists'

# The policy name exceeds the length limit.
INVALIDPARAMETER_POLICYNAMESIZEOVERUPPERLIMIT = 'InvalidParameter.PolicyNameSizeOverUpperLimit'

# Errors occurred when the policy type is modified. Only custom policies can be modified.
INVALIDPARAMETER_POLICYTYPEERROR = 'InvalidParameter.PolicyTypeError'

# The permission configuration does not exist.
INVALIDPARAMETER_ROLECONFIGURATIONNOTEXIST = 'InvalidParameter.RoleConfigurationNotExist'

# The permission configuration still contains policies.
INVALIDPARAMETER_ROLEPOLICYALREADYEXIST = 'InvalidParameter.RolePolicyAlreadyExist'

# The policy does not exist.
INVALIDPARAMETER_ROLEPOLICYNOTEXIST = 'InvalidParameter.RolePolicyNotExist'

# SCIM key does not exist.
INVALIDPARAMETER_SCIMCREDENTIALNOTFOUND = 'InvalidParameter.ScimCredentialNotFound'

# SCIM synchronization status error
INVALIDPARAMETER_SCIMSYNCSTATUSERROR = 'InvalidParameter.ScimSyncStatusError'

# Tag value error.
INVALIDPARAMETER_TAGERROR = 'InvalidParameter.TagError'

# The user still exists in the user group.
INVALIDPARAMETER_USERALREADYEXISTSGROUP = 'InvalidParameter.UserAlreadyExistsGroup'

# SCIM key status error
INVALIDPARAMETER_USERSCIMCREDENTIALSTATUSERROR = 'InvalidParameter.UserScimCredentialStatusError'

# The username already exists.
INVALIDPARAMETER_USERNAMEALREADYEXISTS = 'InvalidParameter.UsernameAlreadyExists'

# The username has a format error.
INVALIDPARAMETER_USERNAMEFORMATERROR = 'InvalidParameter.UsernameFormatError'

# The CIC space name already exists. You should change the space name.
INVALIDPARAMETERVALUE_IDENTITYCENTERZONENAMEALREADYEXIST = 'InvalidParameterValue.IdentityCenterZoneNameAlreadyExist'

# The SSO enabling status is invalid.
INVALIDPARAMETERVALUE_SSOSTATUSINVALID = 'InvalidParameterValue.SSoStatusInvalid'

# The X509 certificate has a format error.
INVALIDPARAMETERVALUE_X509CERTIFICATEFORMATERROR = 'InvalidParameterValue.X509CertificateFormatError'

# The space name does not meet specifications.
INVALIDPARAMETERVALUE_ZONENAMEFORMATERROR = 'InvalidParameterValue.ZoneNameFormatError'

# Requests for adding users to the user group exceed the limit.
LIMITEXCEEDED_ADDUSERTOGROUPLIMITEXCEEDED = 'LimitExceeded.AddUserToGroupLimitExceeded'

# The number of members to be created exceeds the upper limit.
LIMITEXCEEDED_CREATEMEMBEROVERLIMIT = 'LimitExceeded.CreateMemberOverLimit'

# The number of delegated admins for the service exceeds the limit.
LIMITEXCEEDED_CREATEORGSERVICEASSIGNOVERLIMIT = 'LimitExceeded.CreateOrgServiceAssignOverLimit'

# Requests for creating permission configurations exceed the limit.
LIMITEXCEEDED_CREATEROLEASSIGNMENTLIMITEXCEEDED = 'LimitExceeded.CreateRoleAssignmentLimitExceeded'

# Requests for creating users exceed the limit.
LIMITEXCEEDED_CREATEUSERLIMITEXCEEDED = 'LimitExceeded.CreateUserLimitExceeded'

# Requests for creating user synchronization tasks exceed the limit.
LIMITEXCEEDED_CREATEUSERSYNCPROVISIONINGLIMITEXCEEDED = 'LimitExceeded.CreateUserSyncProvisioningLimitExceeded'

# The mailbox configuration exceeds the daily capacity limit.
LIMITEXCEEDED_EMAILBINDOVERLIMIT = 'LimitExceeded.EmailBindOverLimit'

# The number of organization identities exceeds limit.
LIMITEXCEEDED_IDENTITYEXCEEDLIMIT = 'LimitExceeded.IdentityExceedLimit'

# Invitation limit exceeded.
LIMITEXCEEDED_INVITATIONOVERLIMIT = 'LimitExceeded.InvitationOverLimit'

# The department has too many levels.
LIMITEXCEEDED_NODEDEPTHEXCEEDLIMIT = 'LimitExceeded.NodeDepthExceedLimit'

# The number of departments exceeds the upper limit.
LIMITEXCEEDED_NODEEXCEEDLIMIT = 'LimitExceeded.NodeExceedLimit'

# The number of members exceeds the upper limit.
LIMITEXCEEDED_ORGANIZATIONMEMBEROVERLIMIT = 'LimitExceeded.OrganizationMemberOverLimit'

# The number of mobile phones exceeds the binding upper limit.
LIMITEXCEEDED_PHONENUMBOUND = 'LimitExceeded.PhoneNumBound'

# Requests for removing users from the user group exceed the limit.
LIMITEXCEEDED_REMOVEUSERFROMGROUPLIMITEXCEEDED = 'LimitExceeded.RemoveUserFromGroupLimitExceeded'

# The number of SCIM keys exceeds the limit.
LIMITEXCEEDED_SCIMCREDENTIALLIMITEXCEEDED = 'LimitExceeded.ScimCredentialLimitExceeded'

# The number of times to resend the activation email exceeds the limit.
LIMITEXCEEDED_SENDEMAILLIMIT = 'LimitExceeded.SendEmailLimit'

# The number of times to resend the activation email within one hour exceeds the limit.
LIMITEXCEEDED_SENDEMAILWITHINONEHOURLIMIT = 'LimitExceeded.SendEmailWithinOneHourLimit'

# The number of shared members for this operation exceeds the upper limit.
LIMITEXCEEDED_SHAREUNITMEMBEROVERLIMIT = 'LimitExceeded.ShareUnitMemberOverLimit'

# The number of shared resources for this operation exceeds the upper limit.
LIMITEXCEEDED_SHAREUNITRESOURCEOVERLIMIT = 'LimitExceeded.ShareUnitResourceOverLimit'

# The number of modifications to member binding information exceeds the limit.
LIMITEXCEEDED_UPDATEEMAILBINDOVERLIMIT = 'LimitExceeded.UpdateEmailBindOverLimit'

# Operation denied.
OPERATIONDENIED = 'OperationDenied'

# The resource does not exist.
RESOURCENOTFOUND = 'ResourceNotFound'

# The mailbox binding record does not exist.
RESOURCENOTFOUND_EMAILBINDRECORDNOTEXIST = 'ResourceNotFound.EmailBindRecordNotExist'

# The authorizable member identity does not exist.
RESOURCENOTFOUND_MEMBERIDENTITYNOTEXIST = 'ResourceNotFound.MemberIdentityNotExist'

# The member does not exist.
RESOURCENOTFOUND_MEMBERNOTEXIST = 'ResourceNotFound.MemberNotExist'

# The organization member policy does not exist.
RESOURCENOTFOUND_MEMBERPOLICYNOTEXIST = 'ResourceNotFound.MemberPolicyNotExist'

# The authentication subject does not exist.
RESOURCENOTFOUND_ORGANIZATIONAUTHRELATIONNOTEXIST = 'ResourceNotFound.OrganizationAuthRelationNotExist'

# Organization identity does not exist.
RESOURCENOTFOUND_ORGANIZATIONIDENTITYNOTEXIST = 'ResourceNotFound.OrganizationIdentityNotExist'

# The organization member does not exist.
RESOURCENOTFOUND_ORGANIZATIONMEMBERNOTEXIST = 'ResourceNotFound.OrganizationMemberNotExist'

# The organization node does not exist.
RESOURCENOTFOUND_ORGANIZATIONNODENOTEXIST = 'ResourceNotFound.OrganizationNodeNotExist'

# The organization does not exist.
RESOURCENOTFOUND_ORGANIZATIONNOTEXIST = 'ResourceNotFound.OrganizationNotExist'

# Organization service delegation does not exist.
RESOURCENOTFOUND_ORGANIZATIONSERVICEASSIGNNOTEXIST = 'ResourceNotFound.OrganizationServiceAssignNotExist'

# The organization service does not exist.
RESOURCENOTFOUND_ORGANIZATIONSERVICENOTEXIST = 'ResourceNotFound.OrganizationServiceNotExist'

# Policy does not exist.
RESOURCENOTFOUND_POLICYNOTEXIST = 'ResourceNotFound.PolicyNotExist'

# The permission authorization record does not exist.
RESOURCENOTFOUND_ROLECONFIGURATIONAUTHORIZATIONNOTFOUND = 'ResourceNotFound.RoleConfigurationAuthorizationNotFound'

# The permission configuration synchronization does not exist.
RESOURCENOTFOUND_ROLECONFIGURATIONPROVISIONINGNOTFOUND = 'ResourceNotFound.RoleConfigurationProvisioningNotFound'

# The permission configuration task does not exist.
RESOURCENOTFOUND_ROLECONFIGURATIONTASKNOTFOUND = 'ResourceNotFound.RoleConfigurationTaskNotFound'

# The SAML identity provider configuration does not exist.
RESOURCENOTFOUND_SAMLIDENTITYPROVIDERNOTFOUND = 'ResourceNotFound.SAMLIdentityProviderNotFound'

# The SAML service provider information does not exist.
RESOURCENOTFOUND_SAMLSERVICEPROVIDERNOTFOUND = 'ResourceNotFound.SAMLServiceProviderNotFound'

# The organization service role does not exist.
RESOURCENOTFOUND_SERVICEROLENOTEXIST = 'ResourceNotFound.ServiceRoleNotExist'

# The user does not exist.
RESOURCENOTFOUND_USERNOTEXIST = 'ResourceNotFound.UserNotExist'

# The user synchronization does not exist.
RESOURCENOTFOUND_USERPROVISIONINGNOTFOUND = 'ResourceNotFound.UserProvisioningNotFound'

# The user synchronization task does not exist.
RESOURCENOTFOUND_USERPROVISIONINGTASKNOTFOUND = 'ResourceNotFound.UserProvisioningTaskNotFound'

# The X509 certificate does not exist.
RESOURCENOTFOUND_X509CERTIFICATENOTFOUND = 'ResourceNotFound.X509CertificateNotFound'

# Resources are unavailable.
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# The payer has a financial status exception and does not support pay-on-behalf.
UNSUPPORTEDOPERATION_ABNORMALFINANCIALSTATUSOFADMIN = 'UnsupportedOperation.AbnormalFinancialStatusOfAdmin'

# Member's financial status is abnormal. Pay-on-behalf mode is not supported.
UNSUPPORTEDOPERATION_ABNORMALFINANCIALSTATUSOFMEMBER = 'UnsupportedOperation.AbnormalFinancialStatusOfMember'

# No paying relationships can be added.
UNSUPPORTEDOPERATION_ADDDELEGATEPAYERNOTALLOW = 'UnsupportedOperation.AddDelegatePayerNotAllow'

# No offer inheritance relationships can be added.
UNSUPPORTEDOPERATION_ADDDISCOUNTINHERITNOTALLOW = 'UnsupportedOperation.AddDiscountInheritNotAllow'

# The resellers of the administrator and the member do not match.
UNSUPPORTEDOPERATION_AGENTNOTSAME = 'UnsupportedOperation.AgentNotSame'

# The created member is not allowed to create an organization.
UNSUPPORTEDOPERATION_CREATEMEMBERNOTALLOWCREATEORGANIZATION = 'UnsupportedOperation.CreateMemberNotAllowCreateOrganization'

# The created member cannot be removed from the organization.
UNSUPPORTEDOPERATION_CREATEMEMBERNOTALLOWDELETE = 'UnsupportedOperation.CreateMemberNotAllowDelete'

# The created member is not allowed to exit.
UNSUPPORTEDOPERATION_CREATEMEMBERNOTALLOWQUIT = 'UnsupportedOperation.CreateMemberNotAllowQuit'

# Deleting the payment relationship is not allowed.
UNSUPPORTEDOPERATION_DELETEDELEGATEPAYERNOTALLOW = 'UnsupportedOperation.DeleteDelegatePayerNotAllow'

# Payment-on-behalf is not supported for this member or payer as it is a reseller.
UNSUPPORTEDOPERATION_EXISTEDAGENT = 'UnsupportedOperation.ExistedAgent'

# Payment-on-behalf is not supported for this member or payer as it is a reseller’s account.
UNSUPPORTEDOPERATION_EXISTEDCLIENT = 'UnsupportedOperation.ExistedClient'

# The user type mismatches.
UNSUPPORTEDOPERATION_INCONSISTENTUSERTYPES = 'UnsupportedOperation.InconsistentUserTypes'

# An error occurred while calling the operations management system.
UNSUPPORTEDOPERATION_MANAGEMENTSYSTEMERROR = 'UnsupportedOperation.ManagementSystemError'

# The member account has an overdue payment.
UNSUPPORTEDOPERATION_MEMBERACCOUNTARREARS = 'UnsupportedOperation.MemberAccountArrears'

# The member has an inherited offer.
UNSUPPORTEDOPERATION_MEMBERDISCOUNTINHERITEXISTED = 'UnsupportedOperation.MemberDiscountInheritExisted'

# The member has an account-level offer.
UNSUPPORTEDOPERATION_MEMBEREXISTACCOUNTLEVELDISCOUNTINHERIT = 'UnsupportedOperation.MemberExistAccountLevelDiscountInherit'

# The member is configured with operation audit and cannot be deleted.
UNSUPPORTEDOPERATION_MEMBEREXISTOPERATEPROCESSNOTALLOWDELETE = 'UnsupportedOperation.MemberExistOperateProcessNotAllowDelete'

# The member is a delegated admin of the organization service and cannot quit the organization.
UNSUPPORTEDOPERATION_MEMBEREXISTSERVICENOTALLOWDELETE = 'UnsupportedOperation.MemberExistServiceNotAllowDelete'

# The member has vouchers. Pay-on-behalf mode is not supported.
UNSUPPORTEDOPERATION_MEMBERHASVOUCHER = 'UnsupportedOperation.MemberHasVoucher'

# The account is an agent or an agent customer.
UNSUPPORTEDOPERATION_MEMBERISAGENT = 'UnsupportedOperation.MemberIsAgent'

# The member is not a reseller customer.
UNSUPPORTEDOPERATION_MEMBERISNOTCLIENT = 'UnsupportedOperation.MemberIsNotClient'

# No credit card is bound to the member.
UNSUPPORTEDOPERATION_MEMBERNOPAYMENT = 'UnsupportedOperation.MemberNoPayment'

# The member does not support voluntary exit.
UNSUPPORTEDOPERATION_MEMBERNOTALLOWQUIT = 'UnsupportedOperation.MemberNotAllowQuit'

# The member does not support the operation.
UNSUPPORTEDOPERATION_MEMBERUNSUPPORTEDOPERATION = 'UnsupportedOperation.MemberUnsupportedOperation'

# There is an ongoing order.
UNSUPPORTEDOPERATION_ORDERINPROGRESSEXISTED = 'UnsupportedOperation.OrderInProgressExisted'

# The admin has an inherited offer.
UNSUPPORTEDOPERATION_OWNERDISCOUNTINHERITEXISTED = 'UnsupportedOperation.OwnerDiscountInheritExisted'

# The payer has an overdue payment and has no credit account.
UNSUPPORTEDOPERATION_PAYERARREARSANDNOCREDITACCOUNT = 'UnsupportedOperation.PayerArrearsAndNoCreditAccount'

# The payer has an account-level offer.
UNSUPPORTEDOPERATION_PAYEREXISTACCOUNTLEVELDISCOUNTINHERIT = 'UnsupportedOperation.PayerExistAccountLevelDiscountInherit'

# Pay-on-behalf is not supported for second-level reseller customers exist.
UNSUPPORTEDOPERATION_SECONDARYDISTRIBUTORSUBCLIENTEXISTED = 'UnsupportedOperation.SecondaryDistributorSubClientExisted'

# Sharing with other organizational members is not supported.
UNSUPPORTEDOPERATION_SHARINGTOOTHERORGANIZATIONMEMBER = 'UnsupportedOperation.SharingToOtherOrganizationMember'
