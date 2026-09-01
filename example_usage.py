from client import CreatorPaidAdWhitelistingTokenBrokerClient

def main():
    client = CreatorPaidAdWhitelistingTokenBrokerClient()
    res = client.broker_ad_whitelisting_token('@tech_reviewer', 'META_PARTNERSHIP_ADS', 90)
    print('Ad Whitelisting Broker: ' + res['token_broker_id'] + ' (' + res['platform_network'] + ')')
    print('Handshake Verified: ' + str(res['identity_handshake_verified']) + ' | Active Codes: ' + str(res['active_whitelisted_ad_codes_count']))
    print('Ad Manager URL: ' + res['ad_manager_integration_url'])

if __name__ == '__main__':
    main()
