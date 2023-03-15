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


# The user has not completed identity verification.
FAILEDOPERATION_AUTHINFOEMPTY = 'FailedOperation.AuthInfoEmpty'

# The user has not completed enterprise identity verification.
FAILEDOPERATION_AUTHNOTENTERPRISE = 'FailedOperation.AuthNotEnterprise'

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

# You cannot quit an organization created by yourself.
FAILEDOPERATION_DISABLEQUITSELFCREATEDORGANIZATION = 'FailedOperation.DisableQuitSelfCreatedOrganization'

# An error occurred while querying the identity information.
FAILEDOPERATION_GETAUTHINFO = 'FailedOperation.GetAuthInfo'

# The member has a payer and cannot be deleted.
FAILEDOPERATION_MEMBEREXISTDELEGATEPAYERNOTALLOWDELETE = 'FailedOperation.MemberExistDelegatePayerNotAllowDelete'

# The member is a payer and cannot be deleted.
FAILEDOPERATION_MEMBERISDELEGATEPAYERNOTALLOWDELETE = 'FailedOperation.MemberIsDelegatePayerNotAllowDelete'

# The name is already in use.
FAILEDOPERATION_MEMBERNAMEUSED = 'FailedOperation.MemberNameUsed'

# The member authorization policy name is already in use.
FAILEDOPERATION_MEMBERPOLICYNAMEEXIST = 'FailedOperation.MemberPolicyNameExist'

# The member is sharing a resource.
FAILEDOPERATION_MEMBERSHARERESOURCE = 'FailedOperation.MemberShareResource'

# There are members in this department
FAILEDOPERATION_NODENOTEMPTY = 'FailedOperation.NodeNotEmpty'

# An error occurred while manipulating the billing member permission.
FAILEDOPERATION_OPERATEBILLINGPERMISSIONERR = 'FailedOperation.OperateBillingPermissionErr'

# Failed to manipulate the policy.
FAILEDOPERATION_OPERATEPOLICY = 'FailedOperation.OperatePolicy'

# The member is an entity admin account and cannot be deleted.
FAILEDOPERATION_ORGANIZATIONAUTHMANAGENOTALLOWDELETE = 'FailedOperation.OrganizationAuthManageNotAllowDelete'

# The member name already exists.
FAILEDOPERATION_ORGANIZATIONMEMBERNAMEUSED = 'FailedOperation.OrganizationMemberNameUsed'

# The number of nodes to be deleted exceeds the upper limit.
FAILEDOPERATION_ORGANIZATIONNODEDELETEOVERLIMIT = 'FailedOperation.OrganizationNodeDeleteOverLimit'

# The node name is already in use.
FAILEDOPERATION_ORGANIZATIONNODENAMEUSED = 'FailedOperation.OrganizationNodeNameUsed'

# There are nodes in the organization.
FAILEDOPERATION_ORGANIZATIONNODENOTEMPTY = 'FailedOperation.OrganizationNodeNotEmpty'

# The organization node does not exist.
FAILEDOPERATION_ORGANIZATIONNODENOTEXIST = 'FailedOperation.OrganizationNodeNotExist'

# The organization permission is invalid.
FAILEDOPERATION_ORGANIZATIONPERMISSIONILLEGAL = 'FailedOperation.OrganizationPermissionIllegal'

# The organization policy is invalid.
FAILEDOPERATION_ORGANIZATIONPOLICYILLEGAL = 'FailedOperation.OrganizationPolicyIllegal'

# The payer is invalid.
FAILEDOPERATION_PAYUINILLEGAL = 'FailedOperation.PayUinIllegal'

# Failed to leave the shared unit.
FAILEDOPERATION_QUITSHAREUINTERROR = 'FailedOperation.QuitShareUintError'

# The member is using a shared resource.
FAILEDOPERATION_SHARERESOURCEMEMBERINUSE = 'FailedOperation.ShareResourceMemberInUse'

# The UIN does not belong to the organization.
FAILEDOPERATION_SOMEUINSNOTINORGANIZATION = 'FailedOperation.SomeUinsNotInOrganization'

# The sub-account has an identity.
FAILEDOPERATION_SUBACCOUNTIDENTITYEXIST = 'FailedOperation.SubAccountIdentityExist'

# The sub-account does not exist.
FAILEDOPERATION_SUBACCOUNTNOTEXIST = 'FailedOperation.SubAccountNotExist'

# An internal error occurred.
INTERNALERROR = 'InternalError'

# The parameter is incorrect.
INVALIDPARAMETER = 'InvalidParameter'

# The number of members to be created exceeds the upper limit.
LIMITEXCEEDED_CREATEMEMBEROVERLIMIT = 'LimitExceeded.CreateMemberOverLimit'

# The department has too many levels.
LIMITEXCEEDED_NODEDEPTHEXCEEDLIMIT = 'LimitExceeded.NodeDepthExceedLimit'

# The number of departments exceeds the upper limit.
LIMITEXCEEDED_NODEEXCEEDLIMIT = 'LimitExceeded.NodeExceedLimit'

# The number of members exceeds the upper limit.
LIMITEXCEEDED_ORGANIZATIONMEMBEROVERLIMIT = 'LimitExceeded.OrganizationMemberOverLimit'

# The authorizable member identity does not exist.
RESOURCENOTFOUND_MEMBERIDENTITYNOTEXIST = 'ResourceNotFound.MemberIdentityNotExist'

# The member does not exist.
RESOURCENOTFOUND_MEMBERNOTEXIST = 'ResourceNotFound.MemberNotExist'

# The organization member policy does not exist.
RESOURCENOTFOUND_MEMBERPOLICYNOTEXIST = 'ResourceNotFound.MemberPolicyNotExist'

# The organization member does not exist.
RESOURCENOTFOUND_ORGANIZATIONMEMBERNOTEXIST = 'ResourceNotFound.OrganizationMemberNotExist'

# The organization node does not exist.
RESOURCENOTFOUND_ORGANIZATIONNODENOTEXIST = 'ResourceNotFound.OrganizationNodeNotExist'

# The organization does not exist.
RESOURCENOTFOUND_ORGANIZATIONNOTEXIST = 'ResourceNotFound.OrganizationNotExist'

# The organization service does not exist.
RESOURCENOTFOUND_ORGANIZATIONSERVICENOTEXIST = 'ResourceNotFound.OrganizationServiceNotExist'

# The operation is not supported.
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# No paying relationships can be added.
UNSUPPORTEDOPERATION_ADDDELEGATEPAYERNOTALLOW = 'UnsupportedOperation.AddDelegatePayerNotAllow'

# No offer inheritance relationships can be added.
UNSUPPORTEDOPERATION_ADDDISCOUNTINHERITNOTALLOW = 'UnsupportedOperation.AddDiscountInheritNotAllow'

# Created members cannot be deleted.
UNSUPPORTEDOPERATION_CREATEMEMBERNOTALLOWDELETE = 'UnsupportedOperation.CreateMemberNotAllowDelete'

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

# The organization member is assigned with an organization service and cannot leave.
UNSUPPORTEDOPERATION_MEMBEREXISTSERVICENOTALLOWDELETE = 'UnsupportedOperation.MemberExistServiceNotAllowDelete'

# The member is an agent or customer.
UNSUPPORTEDOPERATION_MEMBERISAGENT = 'UnsupportedOperation.MemberIsAgent'

# No credit card is bound to the member.
UNSUPPORTEDOPERATION_MEMBERNOPAYMENT = 'UnsupportedOperation.MemberNoPayment'

# There is an ongoing order.
UNSUPPORTEDOPERATION_ORDERINPROGRESSEXISTED = 'UnsupportedOperation.OrderInProgressExisted'

# The admin has an inherited offer.
UNSUPPORTEDOPERATION_OWNERDISCOUNTINHERITEXISTED = 'UnsupportedOperation.OwnerDiscountInheritExisted'

# The payer has an overdue payment and has no credit account.
UNSUPPORTEDOPERATION_PAYERARREARSANDNOCREDITACCOUNT = 'UnsupportedOperation.PayerArrearsAndNoCreditAccount'

# The payer has an account-level offer.
UNSUPPORTEDOPERATION_PAYEREXISTACCOUNTLEVELDISCOUNTINHERIT = 'UnsupportedOperation.PayerExistAccountLevelDiscountInherit'
