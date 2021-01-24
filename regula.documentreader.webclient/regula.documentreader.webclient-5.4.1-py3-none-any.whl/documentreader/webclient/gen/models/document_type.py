# coding: utf-8

"""
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from regula.documentreader.webclient.gen.configuration import Configuration
# this line was added to enable pycharm type hinting
from regula.documentreader.webclient.gen.models import *


class DocumentType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    ""
    NOT_DEFINED = int("0")

    ""
    PASSPORT = int("11")

    ""
    IDENTITY_CARD = int("12")

    ""
    DIPLOMATIC_PASSPORT = int("13")

    ""
    SERVICE_PASSPORT = int("14")

    ""
    SEAMANS_IDENTITY_DOCUMENT = int("15")

    ""
    IDENTITY_CARD_FOR_RESIDENCE = int("16")

    ""
    TRAVEL_DOCUMENT = int("17")

    ""
    OTHER = int("99")

    ""
    VISA_ID2 = int("29")

    ""
    VISA_ID3 = int("30")

    ""
    NATIONAL_IDENTITY_CARD = int("20")

    ""
    SOCIAL_IDENTITY_CARD = int("21")

    ""
    ALIENS_IDENTITY_CARD = int("22")

    ""
    PRIVILEGED_IDENTITY_CARD = int("23")

    ""
    RESIDENCE_PERMIT_IDENTITY_CARD = int("24")

    ""
    ORIGIN_CARD = int("25")

    ""
    EMERGENCY_PASSPORT = int("26")

    ""
    ALIENS_PASSPORT = int("27")

    ""
    ALTERNATIVE_IDENTITY_CARD = int("28")

    ""
    AUTHORIZATION_CARD = int("32")

    ""
    BEGINNER_PERMIT = int("33")

    ""
    BORDER_CROSSING_CARD = int("34")

    ""
    CHAUFFEUR_LICENSE = int("35")

    ""
    CHAUFFEUR_LICENSE_UNDER_18 = int("36")

    ""
    CHAUFFEUR_LICENSE_UNDER_21 = int("37")

    ""
    COMMERCIAL_DRIVING_LICENSE = int("38")

    ""
    COMMERCIAL_DRIVING_LICENSE_INSTRUCTIONAL_PERMIT = int("39")

    ""
    COMMERCIAL_DRIVING_LICENSE_UNDER_18 = int("40")

    ""
    COMMERCIAL_DRIVING_LICENSE_UNDER_21 = int("41")

    ""
    COMMERCIAL_INSTRUCTION_PERMIT = int("42")

    ""
    COMMERCIAL_NEW_PERMIT = int("43")

    ""
    CONCEALED_CARRY_LICENSE = int("44")

    ""
    CONCEALED_FIREARM_PERMIT = int("45")

    ""
    CONDITIONAL_DRIVING_LICENSE = int("46")

    ""
    DEPARTMENT_OF_VETERANS_AFFAIRS_IDENTITY_CARD = int("47")

    ""
    DIPLOMATIC_DRIVING_LICENSE = int("48")

    ""
    DRIVING_LICENSE = int("49")

    ""
    DRIVING_LICENSE_INSTRUCTIONAL_PERMIT = int("50")

    ""
    DRIVING_LICENSE_INSTRUCTIONAL_PERMIT_UNDER_18 = int("51")

    ""
    DRIVING_LICENSE_INSTRUCTIONAL_PERMIT_UNDER_21 = int("52")

    ""
    DRIVING_LICENSE_LEARNERS_PERMIT = int("53")

    ""
    DRIVING_LICENSE_LEARNERS_PERMIT_UNDER_18 = int("54")

    ""
    DRIVING_LICENSE_LEARNERS_PERMIT_UNDER_21 = int("55")

    ""
    DRIVING_LICENSE_NOVICE = int("56")

    ""
    DRIVING_LICENSE_NOVICE_UNDER_18 = int("57")

    ""
    DRIVING_LICENSE_NOVICE_UNDER_21 = int("58")

    ""
    DRIVING_LICENSE_REGISTERED_OFFENDER = int("59")

    ""
    DRIVING_LICENSE_RESTRICTED_UNDER_18 = int("60")

    ""
    DRIVING_LICENSE_RESTRICTED_UNDER_21 = int("61")

    ""
    DRIVING_LICENSE_TEMPORARY_VISITOR = int("62")

    ""
    DRIVING_LICENSE_TEMPORARY_VISITOR_UNDER_18 = int("63")

    ""
    DRIVING_LICENSE_TEMPORARY_VISITOR_UNDER_21 = int("64")

    ""
    DRIVING_LICENSE_UNDER_18 = int("65")

    ""
    DRIVING_LICENSE_UNDER_21 = int("66")

    ""
    EMPLOYMENT_DRIVING_PERMIT = int("67")

    ""
    ENHANCED_CHAUFFEUR_LICENSE = int("68")

    ""
    ENHANCED_CHAUFFEUR_LICENSE_UNDER_18 = int("69")

    ""
    ENHANCED_CHAUFFEUR_LICENSE_UNDER_21 = int("70")

    ""
    ENHANCED_COMMERCIAL_DRIVING_LICENSE = int("71")

    ""
    ENHANCED_DRIVING_LICENSE = int("72")

    ""
    ENHANCED_DRIVING_LICENSE_UNDER_18 = int("73")

    ""
    ENHANCED_DRIVING_LICENSE_UNDER_21 = int("74")

    ""
    ENHANCED_IDENTITY_CARD = int("75")

    ""
    ENHANCED_IDENTITY_CARD_UNDER_18 = int("76")

    ""
    ENHANCED_IDENTITY_CARD_UNDER_21 = int("77")

    ""
    ENHANCED_OPERATORS_LICENSE = int("78")

    ""
    FIREARMS_PERMIT = int("79")

    ""
    FULL_PROVISIONAL_LICENSE = int("80")

    ""
    FULL_PROVISIONAL_LICENSE_UNDER_18 = int("81")

    ""
    FULL_PROVISIONAL_LICENSE_UNDER_21 = int("82")

    ""
    GENEVA_CONVENTIONS_IDENTITY_CARD = int("83")

    ""
    GRADUATED_DRIVING_LICENSE_UNDER_18 = int("84")

    ""
    GRADUATED_DRIVING_LICENSE_UNDER_21 = int("85")

    ""
    GRADUATED_INSTRUCTION_PERMIT_UNDER_18 = int("86")

    ""
    GRADUATED_INSTRUCTION_PERMIT_UNDER_21 = int("87")

    ""
    GRADUATED_LICENSE_UNDER_18 = int("88")

    ""
    GRADUATED_LICENSE_UNDER_21 = int("89")

    ""
    HANDGUN_CARRY_PERMIT = int("90")

    ""
    IDENTITY_AND_PRIVILEGE_CARD = int("91")

    ""
    IDENTITY_CARD_MOBILITY_IMPAIRED = int("92")

    ""
    IDENTITY_CARD_REGISTERED_OFFENDER = int("93")

    ""
    IDENTITY_CARD_TEMPORARY_VISITOR = int("94")

    ""
    IDENTITY_CARD_TEMPORARY_VISITOR_UNDER_18 = int("95")

    ""
    IDENTITY_CARD_TEMPORARY_VISITOR_UNDER_21 = int("96")

    ""
    IDENTITY_CARD_UNDER_18 = int("97")

    ""
    IDENTITY_CARD_UNDER_21 = int("98")

    ""
    IGNITION_INTERLOCK_PERMIT = int("100")

    ""
    IMMIGRANT_VISA = int("101")

    ""
    INSTRUCTION_PERMIT = int("102")

    ""
    INSTRUCTION_PERMIT_UNDER_18 = int("103")

    ""
    INSTRUCTION_PERMIT_UNDER_21 = int("104")

    ""
    INTERIM_DRIVING_LICENSE = int("105")

    ""
    INTERIM_IDENTITY_CARD = int("106")

    ""
    INTERMEDIATE_DRIVING_LICENSE = int("107")

    ""
    INTERMEDIATE_DRIVING_LICENSE_UNDER_18 = int("108")

    ""
    INTERMEDIATE_DRIVING_LICENSE_UNDER_21 = int("109")

    ""
    JUNIOR_DRIVING_LICENSE = int("110")

    ""
    LEARNER_INSTRUCTIONAL_PERMIT = int("111")

    ""
    LEARNER_LICENSE = int("112")

    ""
    LEARNER_LICENSE_UNDER_18 = int("113")

    ""
    LEARNER_LICENSE_UNDER_21 = int("114")

    ""
    LEARNER_PERMIT = int("115")

    ""
    LEARNER_PERMIT_UNDER_18 = int("116")

    ""
    LEARNER_PERMIT_UNDER_21 = int("117")

    ""
    LIMITED_LICENSE = int("118")

    ""
    LIMITED_PERMIT = int("119")

    ""
    LIMITED_TERM_DRIVING_LICENSE = int("120")

    ""
    LIMITED_TERM_IDENTITY_CARD = int("121")

    ""
    LIQUOR_IDENTITY_CARD = int("122")

    ""
    NEW_PERMIT = int("123")

    ""
    NEW_PERMIT_UNDER_18 = int("124")

    ""
    NEW_PERMIT_UNDER_21 = int("125")

    ""
    NON_US_CITIZEN_DRIVING_LICENSE = int("126")

    ""
    OCCUPATIONAL_DRIVING_LICENSE = int("127")

    ""
    ONEIDA_TRIBE_OF_INDIANS_IDENTITY_CARD = int("128")

    ""
    OPERATOR_LICENSE = int("129")

    ""
    OPERATOR_LICENSE_UNDER_18 = int("130")

    ""
    OPERATOR_LICENSE_UNDER_21 = int("131")

    ""
    PERMANENT_DRIVING_LICENSE = int("132")

    ""
    PERMIT_TO_REENTER = int("133")

    ""
    PROBATIONARY_AUTO_LICENSE = int("134")

    ""
    PROBATIONARY_DRIVING_LICENSE_UNDER_18 = int("135")

    ""
    PROBATIONARY_DRIVING_LICENSE_UNDER_21 = int("136")

    ""
    PROBATIONARY_VEHICLE_SALES_PERSON_LICENSE = int("137")

    ""
    PROVISIONAL_DRIVING_LICENSE = int("138")

    ""
    PROVISIONAL_DRIVING_LICENSE_UNDER_18 = int("139")

    ""
    PROVISIONAL_DRIVING_LICENSE_UNDER_21 = int("140")

    ""
    PROVISIONAL_LICENSE = int("141")

    ""
    PROVISIONAL_LICENSE_UNDER_18 = int("142")

    ""
    PROVISIONAL_LICENSE_UNDER_21 = int("143")

    ""
    PUBLIC_PASSENGER_CHAUFFEUR_LICENSE = int("144")

    ""
    RACING_AND_GAMING_COMISSION_CARD = int("145")

    ""
    REFUGEE_TRAVEL_DOCUMENT = int("146")

    ""
    RENEWAL_PERMIT = int("147")

    ""
    RESTRICTED_COMMERCIAL_DRIVER_LICENSE = int("148")

    ""
    RESTRICTED_DRIVER_LICENSE = int("149")

    ""
    RESTRICTED_PERMIT = int("150")

    ""
    SEASONAL_PERMIT = int("151")

    ""
    SEASONAL_RESIDENT_IDENTITY_CARD = int("152")

    ""
    SEASONAL_CITIZEN_IDENTITY_CARD = int("153")

    ""
    SEX_OFFENDER = int("154")

    ""
    SOCIAL_SECURITY_CARD = int("155")

    ""
    TEMPORARY_DRIVING_LICENSE = int("156")

    ""
    TEMPORARY_DRIVING_LICENSE_UNDER_18 = int("157")

    ""
    TEMPORARY_DRIVING_LICENSE_UNDER_21 = int("158")

    ""
    TEMPORARY_IDENTITY_CARD = int("159")

    ""
    TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD = int("160")

    ""
    TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD_UNDER_18 = int("161")

    ""
    TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD_UNDER_21 = int("162")

    ""
    TEMPORARY_VISITOR_DRIVING_LICENSE = int("163")

    ""
    TEMPORARY_VISITOR_DRIVING_LICENSE_UNDER_18 = int("164")

    ""
    TEMPORARY_VISITOR_DRIVING_LICENSE_UNDER_21 = int("165")

    ""
    UNIFORMED_SERVICES_IDENTITY_CARD = int("166")

    ""
    VEHICLE_SALES_PERSON_LICENSE = int("167")

    ""
    WORKER_IDENTIFICATION_CREDENTIAL = int("168")

    ""
    COMMERCIAL_DRIVING_LICENSE_NOVICE = int("169")

    ""
    COMMERCIAL_DRIVING_LICENSE_NOVICE_UNDER_18 = int("170")

    ""
    COMMERCIAL_DRIVING_LICENSE_NOVICE_UNDER_21 = int("171")

    ""
    PASSPORT_CARD = int("172")

    ""
    PASSPORT_RESIDENT_CARD = int("173")

    ""
    PERSONAL_IDENTIFICATION_VERIFICATION = int("174")

    ""
    TEMPORARY_OPERATOR_LICENSE = int("175")

    ""
    DRIVING_LICENSE_UNDER_19 = int("176")

    ""
    IDENTITY_CARD_UNDER_19 = int("177")

    ""
    VISA = int("178")

    ""
    TEMPORARY_PASSPORT = int("179")

    ""
    VOTING_CARD = int("180")

    ""
    HEALTH_CARD = int("181")

    ""
    CERTIFICATE_OF_CITIZENSHIP = int("182")

    ""
    ADDRESS_CARD = int("183")

    ""
    AIRPORT_IMMIGRATION_CARD = int("184")

    ""
    ALIEN_REGISTRATION_CARD = int("185")

    ""
    APEH_CARD = int("186")

    ""
    COUPON_TO_DRIVING_LICENSE = int("187")

    ""
    CREW_MEMBER_CERTIFICATE = int("188")

    ""
    DOCUMENT_FOR_RETURN = int("189")

    ""
    E_CARD = int("190")

    ""
    EMPLOYMENT_CARD = int("191")

    ""
    HKSAR_IMMIGRATION_FORM = int("192")

    ""
    IMMIGRANT_CARD = int("193")

    ""
    LABOUR_CARD = int("194")

    ""
    LAISSEZ_PASSER = int("195")

    ""
    LAWYER_IDENTITY_CERTIFICATE = int("196")

    ""
    LICENSE_CARD = int("197")

    ""
    PASSPORT_STATELESS = int("198")

    ""
    PASSPORT_CHILD = int("199")

    ""
    PASSPORT_CONSULAR = int("200")

    ""
    PASSPORT_DIPLOMATIC_SERVICE = int("201")

    ""
    PASSPORT_OFFICIAL = int("202")

    ""
    PASSPORT_PROVISIONAL = int("203")

    ""
    PASSPORT_SPECIAL = int("204")

    ""
    PERMISSION_TO_THE_LOCAL_BORDER_TRAFFIC = int("205")

    ""
    REGISTRATION_CERTIFICATE = int("206")

    ""
    SEDESOL_CARD = int("207")

    ""
    SOCIAL_CARD = int("208")

    ""
    TB_CARD = int("209")

    ""
    VEHICLE_PASSPORT = int("210")

    ""
    W_DOCUMENT = int("211")

    ""
    DIPLOMATIC_IDENTITY_CARD = int("212")

    ""
    CONSULAR_IDENTITY_CARD = int("213")

    ""
    INCOME_TAX_CARD = int("214")

    ""
    RESIDENCE_PERMIT = int("215")

    ""
    DOCUMENT_OF_IDENTITY = int("216")

    ""
    BORDER_CROSSING_PERMIT = int("217")

    ""
    PASSPORT_LIMITED_VALIDITY = int("218")

    ""
    SIM_CARD = int("219")

    ""
    TAX_CARD = int("220")

    ""
    COMPANY_CARD = int("221")

    ""
    DOMESTIC_PASSPORT = int("222")

    ""
    IDENTITY_CERTIFICATE = int("223")

    ""
    RESIDENT_ID_CARD = int("224")

    ""
    ARMED_FORCES_IDENTITY_CARD = int("225")

    ""
    PROFESSIONAL_CARD = int("226")

    ""
    REGISTRATION_STAMP = int("227")

    ""
    DRIVER_CARD = int("228")

    ""
    DRIVER_TRAINING_CERTIFICATE = int("229")

    ""
    QUALIFICATION_DRIVING_LICENSE = int("230")

    ""
    MEMBERSHIP_CARD = int("231")

    ""
    PUBLIC_VEHICLE_DRIVER_AUTHORITY_CARD = int("232")

    ""
    MARINE_LICENSE = int("233")

    ""
    TEMPORARY_LEARNER_LICENSE = int("234")

    ""
    TEMPORARY_COMMERCIAL_DRIVING_LICENSE = int("235")

    ""
    INTERIM_INSTRUCTIONAL_PERMIT = int("236")

    ""
    CERTIFICATE_OF_COMPETENCY = int("237")

    ""
    CERTIFICATE_OF_PROFICIENCY = int("238")

    allowable_values = [NOT_DEFINED, PASSPORT, IDENTITY_CARD, DIPLOMATIC_PASSPORT, SERVICE_PASSPORT, SEAMANS_IDENTITY_DOCUMENT, IDENTITY_CARD_FOR_RESIDENCE, TRAVEL_DOCUMENT, OTHER, VISA_ID2, VISA_ID3, NATIONAL_IDENTITY_CARD, SOCIAL_IDENTITY_CARD, ALIENS_IDENTITY_CARD, PRIVILEGED_IDENTITY_CARD, RESIDENCE_PERMIT_IDENTITY_CARD, ORIGIN_CARD, EMERGENCY_PASSPORT, ALIENS_PASSPORT, ALTERNATIVE_IDENTITY_CARD, AUTHORIZATION_CARD, BEGINNER_PERMIT, BORDER_CROSSING_CARD, CHAUFFEUR_LICENSE, CHAUFFEUR_LICENSE_UNDER_18, CHAUFFEUR_LICENSE_UNDER_21, COMMERCIAL_DRIVING_LICENSE, COMMERCIAL_DRIVING_LICENSE_INSTRUCTIONAL_PERMIT, COMMERCIAL_DRIVING_LICENSE_UNDER_18, COMMERCIAL_DRIVING_LICENSE_UNDER_21, COMMERCIAL_INSTRUCTION_PERMIT, COMMERCIAL_NEW_PERMIT, CONCEALED_CARRY_LICENSE, CONCEALED_FIREARM_PERMIT, CONDITIONAL_DRIVING_LICENSE, DEPARTMENT_OF_VETERANS_AFFAIRS_IDENTITY_CARD, DIPLOMATIC_DRIVING_LICENSE, DRIVING_LICENSE, DRIVING_LICENSE_INSTRUCTIONAL_PERMIT, DRIVING_LICENSE_INSTRUCTIONAL_PERMIT_UNDER_18, DRIVING_LICENSE_INSTRUCTIONAL_PERMIT_UNDER_21, DRIVING_LICENSE_LEARNERS_PERMIT, DRIVING_LICENSE_LEARNERS_PERMIT_UNDER_18, DRIVING_LICENSE_LEARNERS_PERMIT_UNDER_21, DRIVING_LICENSE_NOVICE, DRIVING_LICENSE_NOVICE_UNDER_18, DRIVING_LICENSE_NOVICE_UNDER_21, DRIVING_LICENSE_REGISTERED_OFFENDER, DRIVING_LICENSE_RESTRICTED_UNDER_18, DRIVING_LICENSE_RESTRICTED_UNDER_21, DRIVING_LICENSE_TEMPORARY_VISITOR, DRIVING_LICENSE_TEMPORARY_VISITOR_UNDER_18, DRIVING_LICENSE_TEMPORARY_VISITOR_UNDER_21, DRIVING_LICENSE_UNDER_18, DRIVING_LICENSE_UNDER_21, EMPLOYMENT_DRIVING_PERMIT, ENHANCED_CHAUFFEUR_LICENSE, ENHANCED_CHAUFFEUR_LICENSE_UNDER_18, ENHANCED_CHAUFFEUR_LICENSE_UNDER_21, ENHANCED_COMMERCIAL_DRIVING_LICENSE, ENHANCED_DRIVING_LICENSE, ENHANCED_DRIVING_LICENSE_UNDER_18, ENHANCED_DRIVING_LICENSE_UNDER_21, ENHANCED_IDENTITY_CARD, ENHANCED_IDENTITY_CARD_UNDER_18, ENHANCED_IDENTITY_CARD_UNDER_21, ENHANCED_OPERATORS_LICENSE, FIREARMS_PERMIT, FULL_PROVISIONAL_LICENSE, FULL_PROVISIONAL_LICENSE_UNDER_18, FULL_PROVISIONAL_LICENSE_UNDER_21, GENEVA_CONVENTIONS_IDENTITY_CARD, GRADUATED_DRIVING_LICENSE_UNDER_18, GRADUATED_DRIVING_LICENSE_UNDER_21, GRADUATED_INSTRUCTION_PERMIT_UNDER_18, GRADUATED_INSTRUCTION_PERMIT_UNDER_21, GRADUATED_LICENSE_UNDER_18, GRADUATED_LICENSE_UNDER_21, HANDGUN_CARRY_PERMIT, IDENTITY_AND_PRIVILEGE_CARD, IDENTITY_CARD_MOBILITY_IMPAIRED, IDENTITY_CARD_REGISTERED_OFFENDER, IDENTITY_CARD_TEMPORARY_VISITOR, IDENTITY_CARD_TEMPORARY_VISITOR_UNDER_18, IDENTITY_CARD_TEMPORARY_VISITOR_UNDER_21, IDENTITY_CARD_UNDER_18, IDENTITY_CARD_UNDER_21, IGNITION_INTERLOCK_PERMIT, IMMIGRANT_VISA, INSTRUCTION_PERMIT, INSTRUCTION_PERMIT_UNDER_18, INSTRUCTION_PERMIT_UNDER_21, INTERIM_DRIVING_LICENSE, INTERIM_IDENTITY_CARD, INTERMEDIATE_DRIVING_LICENSE, INTERMEDIATE_DRIVING_LICENSE_UNDER_18, INTERMEDIATE_DRIVING_LICENSE_UNDER_21, JUNIOR_DRIVING_LICENSE, LEARNER_INSTRUCTIONAL_PERMIT, LEARNER_LICENSE, LEARNER_LICENSE_UNDER_18, LEARNER_LICENSE_UNDER_21, LEARNER_PERMIT, LEARNER_PERMIT_UNDER_18, LEARNER_PERMIT_UNDER_21, LIMITED_LICENSE, LIMITED_PERMIT, LIMITED_TERM_DRIVING_LICENSE, LIMITED_TERM_IDENTITY_CARD, LIQUOR_IDENTITY_CARD, NEW_PERMIT, NEW_PERMIT_UNDER_18, NEW_PERMIT_UNDER_21, NON_US_CITIZEN_DRIVING_LICENSE, OCCUPATIONAL_DRIVING_LICENSE, ONEIDA_TRIBE_OF_INDIANS_IDENTITY_CARD, OPERATOR_LICENSE, OPERATOR_LICENSE_UNDER_18, OPERATOR_LICENSE_UNDER_21, PERMANENT_DRIVING_LICENSE, PERMIT_TO_REENTER, PROBATIONARY_AUTO_LICENSE, PROBATIONARY_DRIVING_LICENSE_UNDER_18, PROBATIONARY_DRIVING_LICENSE_UNDER_21, PROBATIONARY_VEHICLE_SALES_PERSON_LICENSE, PROVISIONAL_DRIVING_LICENSE, PROVISIONAL_DRIVING_LICENSE_UNDER_18, PROVISIONAL_DRIVING_LICENSE_UNDER_21, PROVISIONAL_LICENSE, PROVISIONAL_LICENSE_UNDER_18, PROVISIONAL_LICENSE_UNDER_21, PUBLIC_PASSENGER_CHAUFFEUR_LICENSE, RACING_AND_GAMING_COMISSION_CARD, REFUGEE_TRAVEL_DOCUMENT, RENEWAL_PERMIT, RESTRICTED_COMMERCIAL_DRIVER_LICENSE, RESTRICTED_DRIVER_LICENSE, RESTRICTED_PERMIT, SEASONAL_PERMIT, SEASONAL_RESIDENT_IDENTITY_CARD, SEASONAL_CITIZEN_IDENTITY_CARD, SEX_OFFENDER, SOCIAL_SECURITY_CARD, TEMPORARY_DRIVING_LICENSE, TEMPORARY_DRIVING_LICENSE_UNDER_18, TEMPORARY_DRIVING_LICENSE_UNDER_21, TEMPORARY_IDENTITY_CARD, TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD, TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD_UNDER_18, TEMPORARY_INSTRUCTION_PERMIT_IDENTITY_CARD_UNDER_21, TEMPORARY_VISITOR_DRIVING_LICENSE, TEMPORARY_VISITOR_DRIVING_LICENSE_UNDER_18, TEMPORARY_VISITOR_DRIVING_LICENSE_UNDER_21, UNIFORMED_SERVICES_IDENTITY_CARD, VEHICLE_SALES_PERSON_LICENSE, WORKER_IDENTIFICATION_CREDENTIAL, COMMERCIAL_DRIVING_LICENSE_NOVICE, COMMERCIAL_DRIVING_LICENSE_NOVICE_UNDER_18, COMMERCIAL_DRIVING_LICENSE_NOVICE_UNDER_21, PASSPORT_CARD, PASSPORT_RESIDENT_CARD, PERSONAL_IDENTIFICATION_VERIFICATION, TEMPORARY_OPERATOR_LICENSE, DRIVING_LICENSE_UNDER_19, IDENTITY_CARD_UNDER_19, VISA, TEMPORARY_PASSPORT, VOTING_CARD, HEALTH_CARD, CERTIFICATE_OF_CITIZENSHIP, ADDRESS_CARD, AIRPORT_IMMIGRATION_CARD, ALIEN_REGISTRATION_CARD, APEH_CARD, COUPON_TO_DRIVING_LICENSE, CREW_MEMBER_CERTIFICATE, DOCUMENT_FOR_RETURN, E_CARD, EMPLOYMENT_CARD, HKSAR_IMMIGRATION_FORM, IMMIGRANT_CARD, LABOUR_CARD, LAISSEZ_PASSER, LAWYER_IDENTITY_CERTIFICATE, LICENSE_CARD, PASSPORT_STATELESS, PASSPORT_CHILD, PASSPORT_CONSULAR, PASSPORT_DIPLOMATIC_SERVICE, PASSPORT_OFFICIAL, PASSPORT_PROVISIONAL, PASSPORT_SPECIAL, PERMISSION_TO_THE_LOCAL_BORDER_TRAFFIC, REGISTRATION_CERTIFICATE, SEDESOL_CARD, SOCIAL_CARD, TB_CARD, VEHICLE_PASSPORT, W_DOCUMENT, DIPLOMATIC_IDENTITY_CARD, CONSULAR_IDENTITY_CARD, INCOME_TAX_CARD, RESIDENCE_PERMIT, DOCUMENT_OF_IDENTITY, BORDER_CROSSING_PERMIT, PASSPORT_LIMITED_VALIDITY, SIM_CARD, TAX_CARD, COMPANY_CARD, DOMESTIC_PASSPORT, IDENTITY_CERTIFICATE, RESIDENT_ID_CARD, ARMED_FORCES_IDENTITY_CARD, PROFESSIONAL_CARD, REGISTRATION_STAMP, DRIVER_CARD, DRIVER_TRAINING_CERTIFICATE, QUALIFICATION_DRIVING_LICENSE, MEMBERSHIP_CARD, PUBLIC_VEHICLE_DRIVER_AUTHORITY_CARD, MARINE_LICENSE, TEMPORARY_LEARNER_LICENSE, TEMPORARY_COMMERCIAL_DRIVING_LICENSE, INTERIM_INSTRUCTIONAL_PERMIT, CERTIFICATE_OF_COMPETENCY, CERTIFICATE_OF_PROFICIENCY]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """DocumentType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentType):
            return True

        return self.to_dict() != other.to_dict()
