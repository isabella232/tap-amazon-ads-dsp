import json
import os

import singer
from singer import metadata

LOGGER = singer.get_logger()

REPORT_TYPE_DIMENSION_METRICS = {
    'CAMPAIGN': {
        'DIMENSIONS': ['ORDER', 'LINE_ITEM', 'CREATIVE'],
        'METRICS': [ 
            'supplyCost', 'agencyFee', 'amazonPlatformFee',
            'amazonAudienceFee', 'totalFee', '3PFees', 'totalCost',
            'impressions', 'eCPM', 'clickThroughs', 'CTR', 'eCPC',
            'totalPixelViews14d', 'totalPixelClicks14d', 'totalPixelCVR14d',
            'totalPixelCPA14d', 'marketingLandingPageViews14d',
            'marketingLandingPageClicks14d', 'marketingLandingPageCVR14d',
            'marketingLandingPageCPA14d', 'subscriptionPageViews14d',
            'subscriptionPageClicks14d', 'subscriptionPageCVR14d',
            'subscriptionPageCPA14d', 'signUpPageViews14d',
            'signUpPageClicks14d', 'signUpPageCVR14d', 'signUpPageCPA14d',
            'applicationViews14d', 'applicationClicks14d', 'applicationCVR14d',
            'applicationCPA14d', 'gameLoadViews14d', 'gameLoadClicks14d',
            'gameLoadCVR14d', 'gameLoadCPA14d', 'widgetLoadViews14d',
            'widgetLoadClicks14d', 'widgetLoadCVR14d', 'widgetLoadCPA14d',
            'surveyStartViews14d', 'surveyStartClicks14d', 'surveyStartCVR14d',
            'surveyStartCPA14d', 'surveyFinishViews14d',
            'surveyFinishClicks14d', 'surveyFinishCVR14d',
            'surveyFinishCPA14d', 'bannerInteractionViews14d',
            'bannerInteractionClicks14d', 'bannerInteractionCVR14d',
            'bannerInteractionCPA14d', 'widgetInteractionViews14d',
            'widgetInteractionClicks14d', 'widgetInteractionCVR14d',
            'widgetInteractionCPA14d', 'gameInteractionViews14d',
            'gameInteractionClicks14d', 'gameInteractionCVR14d',
            'gameInteractionCPA14d', 'emailLoadViews14d', 'emailLoadClicks14d',
            'emailLoadCVR14d', 'emailLoadCPA14d', 'emailInteractionViews14d',
            'emailInteractionClicks14d', 'emailInteractionCVR14d',
            'emailInteractionCPA14d', 'submitButtonViews14d',
            'submitButtonClicks14d', 'submitButtonCVR14d',
            'submitButtonCPA14d', 'purchaseButtonViews14d',
            'purchaseButtonClicks14d', 'purchaseButtonCVR14d',
            'purchaseButtonCPA14d', 'clickOnRedirectViews14d',
            'clickOnRedirectClicks14d', 'clickOnRedirectCVR14d',
            'clickOnRedirectCPA14d', 'signUpButtonViews14d',
            'signUpButtonClicks14d', 'signUpButtonCVR14d',
            'signUpButtonCPA14d', 'subscriptionButtonViews14d',
            'subscriptionButtonClicks14d', 'subscriptionButtonCVR14d',
            'subscriptionButtonCPA14d', 'successPageViews14d',
            'successPageClicks14d', 'successPageCVR14d', 'successPageCPA14d',
            'thankYouPageViews14d', 'thankYouPageClicks14d',
            'thankYouPageCVR14d', 'thankYouPageCPA14d',
            'registrationFormViews14d', 'registrationFormClicks14d',
            'registrationFormCVR14d', 'registrationFormCPA14d',
            'registrationConfirmPageViews14d',
            'registrationConfirmPageClicks14d',
            'registrationConfirmPageCVR14d', 'registrationConfirmPageCPA14d',
            'storeLocatorPageViews14d', 'storeLocatorPageClicks14d',
            'storeLocatorPageCVR14d', 'storeLocatorPageCPA14d',
            'mobileAppFirstStartsCPA14d', 'homepageVisitViews14d',
            'homepageVisitClicks14d', 'homepageVisitCVR14d',
            'homepageVisitCPA14d', 'messageSentViews14d',
            'messageSentClicks14d', 'messageSentCVR14d', 'messageSentCPA14d',
            'referralViews14d', 'referralClicks14d', 'referralCVR14d',
            'referralCPA14d', 'acceptViews14d', 'acceptClicks14d',
            'acceptCVR14d', 'acceptCPA14d', 'declineViews14d',
            'declineClicks14d', 'declineCVR14d', 'declineCPA14d', 'dpv14d',
            'dpvViews14d', 'dpvClicks14d', 'dpvr14d', 'eCPDPV14d', 'pRPV14d',
            'pRPVViews14d', 'pRPVClicks14d', 'pRPVr14d', 'eCPPRPV14d',
            'atl14d', 'atlViews14d', 'atlClicks14d', 'atlr14d', 'eCPAtl14d',
            'atc14d', 'atcViews14d', 'atcClicks14d', 'atcr14d', 'eCPAtc14d',
            'purchases14d', 'purchasesViews14d', 'purchasesClicks14d',
            'purchaseRate14d', 'eCPP14d', 'newToBrandPurchases14d',
            'newToBrandPurchasesViews14d', 'newToBrandPurchasesClicks14d',
            'newToBrandPurchaseRate14d', 'newToBrandECPP14d',
            'percentOfPurchasesNewToBrand14d', 'newSubscribeAndSave14d',
            'newSubscribeAndSaveViews14d', 'newSubscribeAndSaveClicks14d',
            'newSubscribeAndSaveRate14d', 'eCPnewSubscribeAndSave14d',
            'downloadedVideoPlays14d', 'downloadedVideoPlaysViews14d',
            'downloadedVideoPlaysClicks14d', 'downloadedVideoPlayRate14d',
            'eCPDVP14d', 'videoStreams14d', 'videoStreamsViews14d',
            'videoStreamsClicks14d', 'videoStreamsRate14d', 'eCPVS14d',
            'playTrailers14d', 'playTrailersViews14d',
            'playerTrailersClicks14d', 'playTrailerRate14d', 'eCPPT14d',
            'rentals14d', 'rentalsViews14d', 'rentalsClicks14d',
            'rentalRate14d', 'ecpr14d', 'videoDownloads14d',
            'videoDownloadsViews14d', 'videoDownloadsClicks14d',
            'videoDownloadRate14d', 'ecpvd14d', 'videoStart',
            'videoFirstQuartile', 'videoMidpoint', 'videoThirdQuartile',
            'videoComplete', 'videoCompletionRate', 'ecpvc', 'videoPause',
            'videoResume', 'videoMute', 'videoUnmute', 'unitsSold14d',
            'sales14d', 'ROAS14d', 'eRPM14d', 'newToBrandUnitsSold14d',
            'newToBrandProductSales14d', 'newToBrandROAS14d',
            'newToBrandERPM14d', 'totalPRPV14d', 'totalPRPVViews14d',
            'totalPRPVClicks14d', 'totalPRPVr14d', 'totalECPPRPV14d',
            'totalPurchases14d', 'totalPurchasesViews14d',
            'totalPurchasesClicks14d', 'totalPurchaseRate14d', 'totalECPP14d',
            'totalNewToBrandPurchases14d', 'totalNewToBrandPurchasesViews14d',
            'totalNewToBrandPurchasesClicks14d',
            'totalNewToBrandPurchaseRate14d', 'totalNewToBrandECPP14d',
            'totalPercentOfPurchasesNewToBrand14d', 'totalUnitsSold14d',
            'totalSales14d', 'totalROAS14d', 'totalERPM14d',
            'totalNewToBrandUnitsSold14d', 'totalNewToBrandProductSales14d',
            'totalNewToBrandROAS14d', 'totalNewToBrandERPM14d',
            'viewableImpressions', 'measurableImpressions', 'measurableRate',
            'viewabilityRate', 'dropDownSelection14d',
            'dropDownSelectionViews14d', 'dropDownSelectionClicks14d',
            'dropDownSelectionCVR14d', 'dropDownSelectionCPA14d',
            'brandStoreEngagement1', 'brandStoreEngagement1Views',
            'brandStoreEngagement1Clicks', 'brandStoreEngagement1CVR',
            'brandStoreEngagement1CPA', 'brandStoreEngagement2',
            'brandStoreEngagement2Views', 'brandStoreEngagement2Clicks',
            'brandStoreEngagement2CVR', 'brandStoreEngagement2CPA',
            'brandStoreEngagement3', 'brandStoreEngagement3Views',
            'brandStoreEngagement3Clicks', 'brandStoreEngagement3CVR',
            'brandStoreEngagement3CPA', 'brandStoreEngagement4',
            'brandStoreEngagement4Views', 'brandStoreEngagement4Clicks',
            'brandStoreEngagement4CVR', 'brandStoreEngagement4CPA',
            'brandStoreEngagement5', 'brandStoreEngagement5Views',
            'brandStoreEngagement5Clicks', 'brandStoreEngagement5CVR',
            'brandStoreEngagement5CPA', 'brandStoreEngagement6',
            'brandStoreEngagement6Views', 'brandStoreEngagement6Clicks',
            'brandStoreEngagement6CVR', 'brandStoreEngagement6CPA',
            'brandStoreEngagement7', 'brandStoreEngagement7Views',
            'brandStoreEngagement7Clicks', 'brandStoreEngagement7CVR',
            'brandStoreEngagement7CPA', 'productPurchased',
            'productPurchasedViews', 'productPurchasedClicks',
            'productPurchasedCVR', 'productPurchasedCPA', 'videoStarted',
            'videoStartedViews', 'videoStartedClicks', 'videoStartedCVR',
            'videoStartedCPA', 'videoCompleted', 'videoCompletedViews',
            'videoEndClicks', 'videoCompletedCVR', 'videoCompletedCPA',
            'mashupClickToPage', 'mashupClickToPageViews',
            'mashupClickToPageClicks', 'mashupClickToPageCVR',
            'mashupClickToPageCPA', 'mashupBackupImage',
            'mashupBackupImageViews', 'mashupBackupImageClicks',
            'mashupBackupImageCVR', 'mashupBackupImageCPA', '3pFeeAutomotive',
            '3pFeeAutomotiveAbsorbed', '3pFeeComScore',
            '3pFeeComScoreAbsorbed', '3pFeeCPM1', '3pFeeCPM1Absorbed',
            '3pFeeCPM2', '3pFeeCPM2Absorbed', '3pFeeCPM3', '3pFeeCPM3Absorbed',
            '3pFeeDoubleclickCampaignManager',
            '3pFeeDoubleclickCampaignManagerAbsorbed', '3pFeeDoubleVerify',
            '3pFeeDoubleVerifyAbsorbed', '3pFeeIntegralAdScience',
            '3pFeeIntegralAdScienceAbsorbed', 'advertiserTimezone',
            'advertiserCountry'
        ]
    },
    'INVENTORY': {
        'DIMENSIONS': ['ORDER', 'LINE_ITEM', 'SITE', 'SUPPLY'],
        'METRICS': [ 
            'supplyCost', 'agencyFee', 'amazonPlatformFee',
            'amazonAudienceFee', 'totalFee', '3PFees', 'totalCost',
            'impressions', 'eCPM', 'clickThroughs', 'CTR', 'eCPC',
            'totalPixelViews14d', 'totalPixelClicks14d', 'totalPixelCVR14d',
            'totalPixelCPA14d', 'marketingLandingPageViews14d',
            'marketingLandingPageClicks14d', 'marketingLandingPageCVR14d',
            'marketingLandingPageCPA14d', 'subscriptionPageViews14d',
            'subscriptionPageClicks14d', 'subscriptionPageCVR14d',
            'subscriptionPageCPA14d', 'signUpPageViews14d',
            'signUpPageClicks14d', 'signUpPageCVR14d', 'signUpPageCPA14d',
            'applicationViews14d', 'applicationClicks14d', 'applicationCVR14d',
            'applicationCPA14d', 'gameLoadViews14d', 'gameLoadClicks14d',
            'gameLoadCVR14d', 'gameLoadCPA14d', 'widgetLoadViews14d',
            'widgetLoadClicks14d', 'widgetLoadCVR14d', 'widgetLoadCPA14d',
            'surveyStartViews14d', 'surveyStartClicks14d', 'surveyStartCVR14d',
            'surveyStartCPA14d', 'surveyFinishViews14d',
            'surveyFinishClicks14d', 'surveyFinishCVR14d',
            'surveyFinishCPA14d', 'bannerInteractionViews14d',
            'bannerInteractionClicks14d', 'bannerInteractionCVR14d',
            'bannerInteractionCPA14d', 'widgetInteractionViews14d',
            'widgetInteractionClicks14d', 'widgetInteractionCVR14d',
            'widgetInteractionCPA14d', 'gameInteractionViews14d',
            'gameInteractionClicks14d', 'gameInteractionCVR14d',
            'gameInteractionCPA14d', 'emailLoadViews14d', 'emailLoadClicks14d',
            'emailLoadCVR14d', 'emailLoadCPA14d', 'emailInteractionViews14d',
            'emailInteractionClicks14d', 'emailInteractionCVR14d',
            'emailInteractionCPA14d', 'submitButtonViews14d',
            'submitButtonClicks14d', 'submitButtonCVR14d',
            'submitButtonCPA14d', 'purchaseButtonViews14d',
            'purchaseButtonClicks14d', 'purchaseButtonCVR14d',
            'purchaseButtonCPA14d', 'clickOnRedirectViews14d',
            'clickOnRedirectClicks14d', 'clickOnRedirectCVR14d',
            'clickOnRedirectCPA14d', 'signUpButtonViews14d',
            'signUpButtonClicks14d', 'signUpButtonCVR14d',
            'signUpButtonCPA14d', 'subscriptionButtonViews14d',
            'subscriptionButtonClicks14d', 'subscriptionButtonCVR14d',
            'subscriptionButtonCPA14d', 'successPageViews14d',
            'successPageClicks14d', 'successPageCVR14d', 'successPageCPA14d',
            'thankYouPageViews14d', 'thankYouPageClicks14d',
            'thankYouPageCVR14d', 'thankYouPageCPA14d',
            'registrationFormViews14d', 'registrationFormClicks14d',
            'registrationFormCVR14d', 'registrationFormCPA14d',
            'registrationConfirmPageViews14d',
            'registrationConfirmPageClicks14d',
            'registrationConfirmPageCVR14d', 'registrationConfirmPageCPA14d',
            'storeLocatorPageViews14d', 'storeLocatorPageClicks14d',
            'storeLocatorPageCVR14d', 'storeLocatorPageCPA14d',
            'mobileAppFirstStartsCPA14d', 'homepageVisitViews14d',
            'homepageVisitClicks14d', 'homepageVisitCVR14d',
            'homepageVisitCPA14d', 'messageSentViews14d',
            'messageSentClicks14d', 'messageSentCVR14d', 'messageSentCPA14d',
            'referralViews14d', 'referralClicks14d', 'referralCVR14d',
            'referralCPA14d', 'acceptViews14d', 'acceptClicks14d',
            'acceptCVR14d', 'acceptCPA14d', 'declineViews14d',
            'declineClicks14d', 'declineCVR14d', 'declineCPA14d', 'dpv14d',
            'dpvViews14d', 'dpvClicks14d', 'dpvr14d', 'eCPDPV14d', 'pRPV14d',
            'pRPVViews14d', 'pRPVClicks14d', 'pRPVr14d', 'eCPPRPV14d',
            'atl14d', 'atlViews14d', 'atlClicks14d', 'atlr14d', 'eCPAtl14d',
            'atc14d', 'atcViews14d', 'atcClicks14d', 'atcr14d', 'eCPAtc14d',
            'purchases14d', 'purchasesViews14d', 'purchasesClicks14d',
            'purchaseRate14d', 'eCPP14d', 'newToBrandPurchases14d',
            'newToBrandPurchasesViews14d', 'newToBrandPurchasesClicks14d',
            'newToBrandPurchaseRate14d', 'newToBrandECPP14d',
            'percentOfPurchasesNewToBrand14d', 'newSubscribeAndSave14d',
            'newSubscribeAndSaveViews14d', 'newSubscribeAndSaveClicks14d',
            'newSubscribeAndSaveRate14d', 'eCPnewSubscribeAndSave14d',
            'downloadedVideoPlays14d', 'downloadedVideoPlaysViews14d',
            'downloadedVideoPlaysClicks14d', 'downloadedVideoPlayRate14d',
            'eCPDVP14d', 'videoStreams14d', 'videoStreamsViews14d',
            'videoStreamsClicks14d', 'videoStreamsRate14d', 'eCPVS14d',
            'playTrailers14d', 'playTrailersViews14d',
            'playerTrailersClicks14d', 'playTrailerRate14d', 'eCPPT14d',
            'rentals14d', 'rentalsViews14d', 'rentalsClicks14d',
            'rentalRate14d', 'ecpr14d', 'videoDownloads14d',
            'videoDownloadsViews14d', 'videoDownloadsClicks14d',
            'videoDownloadRate14d', 'ecpvd14d', 'videoStart',
            'videoFirstQuartile', 'videoMidpoint', 'videoThirdQuartile',
            'videoComplete', 'videoCompletionRate', 'ecpvc', 'videoPause',
            'videoResume', 'videoMute', 'videoUnmute', 'unitsSold14d',
            'sales14d', 'ROAS14d', 'eRPM14d', 'newToBrandUnitsSold14d',
            'newToBrandProductSales14d', 'newToBrandROAS14d',
            'newToBrandERPM14d', 'totalPRPV14d', 'totalPRPVViews14d',
            'totalPRPVClicks14d', 'totalPRPVr14d', 'totalECPPRPV14d',
            'totalPurchases14d', 'totalPurchasesViews14d',
            'totalPurchasesClicks14d', 'totalPurchaseRate14d', 'totalECPP14d',
            'totalNewToBrandPurchases14d', 'totalNewToBrandPurchasesViews14d',
            'totalNewToBrandPurchasesClicks14d',
            'totalNewToBrandPurchaseRate14d', 'totalNewToBrandECPP14d',
            'totalPercentOfPurchasesNewToBrand14d', 'totalUnitsSold14d',
            'totalSales14d', 'totalROAS14d', 'totalERPM14d',
            'totalNewToBrandUnitsSold14d', 'totalNewToBrandProductSales14d',
            'totalNewToBrandROAS14d', 'totalNewToBrandERPM14d',
            'viewableImpressions', 'measurableImpressions', 'measurableRate',
            'viewabilityRate', 'dropDownSelection14d',
            'dropDownSelectionViews14d', 'dropDownSelectionClicks14d',
            'dropDownSelectionCVR14d', 'dropDownSelectionCPA14d',
            'brandStoreEngagement1', 'brandStoreEngagement1Views',
            'brandStoreEngagement1Clicks', 'brandStoreEngagement1CVR',
            'brandStoreEngagement1CPA', 'brandStoreEngagement2',
            'brandStoreEngagement2Views', 'brandStoreEngagement2Clicks',
            'brandStoreEngagement2CVR', 'brandStoreEngagement2CPA',
            'brandStoreEngagement3', 'brandStoreEngagement3Views',
            'brandStoreEngagement3Clicks', 'brandStoreEngagement3CVR',
            'brandStoreEngagement3CPA', 'brandStoreEngagement4',
            'brandStoreEngagement4Views', 'brandStoreEngagement4Clicks',
            'brandStoreEngagement4CVR', 'brandStoreEngagement4CPA',
            'brandStoreEngagement5', 'brandStoreEngagement5Views',
            'brandStoreEngagement5Clicks', 'brandStoreEngagement5CVR',
            'brandStoreEngagement5CPA', 'brandStoreEngagement6',
            'brandStoreEngagement6Views', 'brandStoreEngagement6Clicks',
            'brandStoreEngagement6CVR', 'brandStoreEngagement6CPA',
            'brandStoreEngagement7', 'brandStoreEngagement7Views',
            'brandStoreEngagement7Clicks', 'brandStoreEngagement7CVR',
            'brandStoreEngagement7CPA', 'productPurchased',
            'productPurchasedViews', 'productPurchasedClicks',
            'productPurchasedCVR', 'productPurchasedCPA', 'videoStarted',
            'videoStartedViews', 'videoStartedClicks', 'videoStartedCVR',
            'videoStartedCPA', 'videoCompleted', 'videoCompletedViews',
            'videoEndClicks', 'videoCompletedCVR', 'videoCompletedCPA',
            'mashupClickToPage', 'mashupClickToPageViews',
            'mashupClickToPageClicks', 'mashupClickToPageCVR',
            'mashupClickToPageCPA', 'mashupBackupImage',
            'mashupBackupImageViews', 'mashupBackupImageClicks',
            'mashupBackupImageCVR', 'mashupBackupImageCPA', 'placementName',
            '3pFeeAutomotive', '3pFeeAutomotiveAbsorbed', '3pFeeComScore',
            '3pFeeComScoreAbsorbed', '3pFeeCPM1', '3pFeeCPM1Absorbed',
            '3pFeeCPM2', '3pFeeCPM2Absorbed', '3pFeeCPM3', '3pFeeCPM3Absorbed',
            '3pFeeDoubleclickCampaignManager',
            '3pFeeDoubleclickCampaignManagerAbsorbed', '3pFeeDoubleVerify',
            '3pFeeDoubleVerifyAbsorbed', '3pFeeIntegralAdScience',
            '3pFeeIntegralAdScienceAbsorbed', 'advertiserTimezone',
            'advertiserCountry'
        ]
    },
    'AUDIENCE': {
        'DIMENSIONS': ['ORDER', 'LINE_ITEM'],
        'METRICS': [ 
            'supplyCost', 'amazonPlatformFee', 'amazonAudienceFee',
            'totalCost', 'impressions', 'eCPM', 'clickThroughs', 'CTR', 'eCPC',
            'totalPixelViews14d', 'totalPixelClicks14d', 'totalPixelCVR14d',
            'totalPixelCPA14d', 'marketingLandingPageViews14d',
            'marketingLandingPageClicks14d', 'marketingLandingPageCVR14d',
            'marketingLandingPageCPA14d', 'subscriptionPageViews14d',
            'subscriptionPageClicks14d', 'subscriptionPageCVR14d',
            'subscriptionPageCPA14d', 'signUpPageViews14d',
            'signUpPageClicks14d', 'signUpPageCVR14d', 'signUpPageCPA14d',
            'applicationViews14d', 'applicationClicks14d', 'applicationCVR14d',
            'applicationCPA14d', 'gameLoadViews14d', 'gameLoadClicks14d',
            'gameLoadCVR14d', 'gameLoadCPA14d', 'widgetLoadViews14d',
            'widgetLoadClicks14d', 'widgetLoadCVR14d', 'widgetLoadCPA14d',
            'surveyStartViews14d', 'surveyStartClicks14d', 'surveyStartCVR14d',
            'surveyStartCPA14d', 'surveyFinishViews14d',
            'surveyFinishClicks14d', 'surveyFinishCVR14d',
            'surveyFinishCPA14d', 'bannerInteractionViews14d',
            'bannerInteractionClicks14d', 'bannerInteractionCVR14d',
            'bannerInteractionCPA14d', 'widgetInteractionViews14d',
            'widgetInteractionClicks14d', 'widgetInteractionCVR14d',
            'widgetInteractionCPA14d', 'gameInteractionViews14d',
            'gameInteractionClicks14d', 'gameInteractionCVR14d',
            'gameInteractionCPA14d', 'emailLoadViews14d', 'emailLoadClicks14d',
            'emailLoadCVR14d', 'emailLoadCPA14d', 'emailInteractionViews14d',
            'emailInteractionClicks14d', 'emailInteractionCVR14d',
            'emailInteractionCPA14d', 'submitButtonViews14d',
            'submitButtonClicks14d', 'submitButtonCVR14d',
            'submitButtonCPA14d', 'purchaseButtonViews14d',
            'purchaseButtonClicks14d', 'purchaseButtonCVR14d',
            'purchaseButtonCPA14d', 'clickOnRedirectViews14d',
            'clickOnRedirectClicks14d', 'clickOnRedirectCVR14d',
            'clickOnRedirectCPA14d', 'signUpButtonViews14d',
            'signUpButtonClicks14d', 'signUpButtonCVR14d',
            'signUpButtonCPA14d', 'subscriptionButtonViews14d',
            'subscriptionButtonClicks14d', 'subscriptionButtonCVR14d',
            'subscriptionButtonCPA14d', 'successPageViews14d',
            'successPageClicks14d', 'successPageCVR14d', 'successPageCPA14d',
            'thankYouPageViews14d', 'thankYouPageClicks14d',
            'thankYouPageCVR14d', 'thankYouPageCPA14d',
            'registrationFormViews14d', 'registrationFormClicks14d',
            'registrationFormCVR14d', 'registrationFormCPA14d',
            'registrationConfirmPageViews14d',
            'registrationConfirmPageClicks14d',
            'registrationConfirmPageCVR14d', 'registrationConfirmPageCPA14d',
            'storeLocatorPageViews14d', 'storeLocatorPageClicks14d',
            'storeLocatorPageCVR14d', 'storeLocatorPageCPA14d',
            'mobileAppFirstStartsCPA14d', 'homepageVisitViews14d',
            'homepageVisitClicks14d', 'homepageVisitCVR14d',
            'homepageVisitCPA14d', 'messageSentViews14d',
            'messageSentClicks14d', 'messageSentCVR14d', 'messageSentCPA14d',
            'referralViews14d', 'referralClicks14d', 'referralCVR14d',
            'referralCPA14d', 'acceptViews14d', 'acceptClicks14d',
            'acceptCVR14d', 'acceptCPA14d', 'declineViews14d',
            'declineClicks14d', 'declineCVR14d', 'declineCPA14d', 'dpv14d',
            'dpvViews14d', 'dpvClicks14d', 'dpvr14d', 'eCPDPV14d', 'pRPV14d',
            'pRPVViews14d', 'pRPVClicks14d', 'pRPVr14d', 'eCPPRPV14d',
            'atl14d', 'atlViews14d', 'atlClicks14d', 'atlr14d', 'eCPAtl14d',
            'atc14d', 'atcViews14d', 'atcClicks14d', 'atcr14d', 'eCPAtc14d',
            'purchases14d', 'purchasesViews14d', 'purchasesClicks14d',
            'purchaseRate14d', 'eCPP14d', 'newToBrandPurchases14d',
            'newToBrandPurchasesViews14d', 'newToBrandPurchasesClicks14d',
            'newToBrandPurchaseRate14d', 'newToBrandECPP14d',
            'percentOfPurchasesNewToBrand14d', 'newSubscribeAndSave14d',
            'newSubscribeAndSaveViews14d', 'newSubscribeAndSaveClicks14d',
            'newSubscribeAndSaveRate14d', 'eCPnewSubscribeAndSave14d',
            'downloadedVideoPlays14d', 'downloadedVideoPlaysViews14d',
            'downloadedVideoPlaysClicks14d', 'downloadedVideoPlayRate14d',
            'eCPDVP14d', 'videoStreams14d', 'videoStreamsViews14d',
            'videoStreamsClicks14d', 'videoStreamsRate14d', 'eCPVS14d',
            'playTrailers14d', 'playTrailersViews14d',
            'playerTrailersClicks14d', 'playTrailerRate14d', 'eCPPT14d',
            'rentals14d', 'rentalsViews14d', 'rentalsClicks14d',
            'rentalRate14d', 'ecpr14d', 'videoDownloads14d',
            'videoDownloadsViews14d', 'videoDownloadsClicks14d',
            'videoDownloadRate14d', 'ecpvd14d', 'videoStart',
            'videoFirstQuartile', 'videoMidpoint', 'videoThirdQuartile',
            'videoComplete', 'videoCompletionRate', 'ecpvc', 'videoPause',
            'videoResume', 'videoMute', 'videoUnmute', 'dropDownSelection14d',
            'dropDownSelectionViews14d', 'dropDownSelectionClicks14d',
            'dropDownSelectionCVR14d', 'dropDownSelectionCPA14d',
            'brandStoreEngagement1', 'brandStoreEngagement1Views',
            'brandStoreEngagement1Clicks', 'brandStoreEngagement1CVR',
            'brandStoreEngagement1CPA', 'brandStoreEngagement2',
            'brandStoreEngagement2Views', 'brandStoreEngagement2Clicks',
            'brandStoreEngagement2CVR', 'brandStoreEngagement2CPA',
            'brandStoreEngagement3', 'brandStoreEngagement3Views',
            'brandStoreEngagement3Clicks', 'brandStoreEngagement3CVR',
            'brandStoreEngagement3CPA', 'brandStoreEngagement4',
            'brandStoreEngagement4Views', 'brandStoreEngagement4Clicks',
            'brandStoreEngagement4CVR', 'brandStoreEngagement4CPA',
            'brandStoreEngagement5', 'brandStoreEngagement5Views',
            'brandStoreEngagement5Clicks', 'brandStoreEngagement5CVR',
            'brandStoreEngagement5CPA', 'brandStoreEngagement6',
            'brandStoreEngagement6Views', 'brandStoreEngagement6Clicks',
            'brandStoreEngagement6CVR', 'brandStoreEngagement6CPA',
            'brandStoreEngagement7', 'brandStoreEngagement7Views',
            'brandStoreEngagement7Clicks', 'brandStoreEngagement7CVR',
            'brandStoreEngagement7CPA', 'productPurchased',
            'productPurchasedViews', 'productPurchasedClicks',
            'productPurchasedCVR', 'productPurchasedCPA', 'videoStarted',
            'videoStartedViews', 'videoStartedClicks', 'videoStartedCVR',
            'videoStartedCPA', 'videoCompleted', 'videoCompletedViews',
            'videoEndClicks', 'videoCompletedCVR', 'videoCompletedCPA',
            'mashupClickToPage', 'mashupClickToPageViews',
            'mashupClickToPageClicks', 'mashupClickToPageCVR',
            'mashupClickToPageCPA', 'mashupBackupImage',
            'mashupBackupImageViews', 'mashupBackupImageClicks',
            'mashupBackupImageCVR', 'mashupBackupImageCPA',
            'advertiserTimezone', 'advertiserCountry'
        ]
    }
}

PRIMARY_KEYS = ['date', 'entityId', 'advertiserId']

DIMENSION_PRIMARY_KEYS = {
    "ORDER": "orderId",
    "LINE_ITEM": "lineItemId",
    "CREATIVE": "creativeID",
    "SITE": "siteName",
    "SUPPLY": "supplySourceName"
}

# Reference:
# https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#Metadata


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def get_schemas(reports):
    schemas = {}
    field_metadata = {}

    # JSON schemas for each report
    for report in reports:
        report_name = report.get('name')
        report_type = report.get('type')
        report_dimensions = report.get('dimensions')

        err = None
        running_error = ''
        if report_type not in REPORT_TYPE_DIMENSION_METRICS:
            err = 'Report: {}, Type: {}: INVALID TYPE'.format(
                report_name, report_type)
            running_error = '{}; {}'.format(running_error, err)
            for dimension in report_dimensions:
                if dimension not in REPORT_TYPE_DIMENSION_METRICS.get(report_type):
                    err = 'Report: {}, Entity: {}, Dimension: {}: INVALID DIMENSION'.format(
                    report_name, report_type, dimension)
                running_error = '{}; {}'.format(running_error, err)
        
        report_path = get_abs_path('schemas/report.json')

        with open(report_path) as file:
            schema = json.load(file)

        schemas[report_name] = schema
        mdata = metadata.new()

        mdata = metadata.get_standard_metadata(
            schema=schema,
            key_properties=['__sdc_record_hash'],
            valid_replication_keys=['date'],
            replication_method='INCREMENTAL')
        field_metadata[report_name] = mdata

    return schemas, field_metadata