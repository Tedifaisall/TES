from web3 import Web3, HTTPProvider
import json
import time
import requests

web3 = Web3(Web3.HTTPProvider(input("Input RPC Url with https:// : "))) #rpc url
chainId = web3.eth.chain_id

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected...\n")
else:
    print("Error Connecting Please Try Again...")
    exit()

print('Auto Wrap Unwrap POL | By ADFMIDN Team')
payerkey = input('Input Privatekey EVM : ')
amount = input('Input Amount Of wPOL For Wrap Unwrap : ')
loop = input('How Many You Want To Transaction ? : ')
print('')
payer = web3.eth.account.from_key(payerkey)
tokenaddr = web3.to_checksum_address("0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270")
tokenaddr2 = web3.to_checksum_address("0x1Cd0cd01c8C902AdAb3430ae04b9ea32CB309CF1")
tokenabi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]')
tokenabi2 = json.loads('[{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"address","name":"trustedForwarder_","type":"address"},{"internalType":"address","name":"underlyingAsset_","type":"address"},{"internalType":"address","name":"treasury_","type":"address"},{"internalType":"address","name":"_permit2","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"target","type":"address"}],"name":"AddressEmptyCode","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"AddressInsufficientBalance","type":"error"},{"inputs":[],"name":"ECDSAInvalidSignature","type":"error"},{"inputs":[{"internalType":"uint256","name":"length","type":"uint256"}],"name":"ECDSAInvalidSignatureLength","type":"error"},{"inputs":[{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"ECDSAInvalidSignatureS","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"allowance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientAllowance","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"needed","type":"uint256"}],"name":"ERC20InsufficientBalance","type":"error"},{"inputs":[{"internalType":"address","name":"approver","type":"address"}],"name":"ERC20InvalidApprover","type":"error"},{"inputs":[{"internalType":"address","name":"receiver","type":"address"}],"name":"ERC20InvalidReceiver","type":"error"},{"inputs":[{"internalType":"address","name":"sender","type":"address"}],"name":"ERC20InvalidSender","type":"error"},{"inputs":[{"internalType":"address","name":"spender","type":"address"}],"name":"ERC20InvalidSpender","type":"error"},{"inputs":[{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"ERC2612ExpiredSignature","type":"error"},{"inputs":[{"internalType":"address","name":"signer","type":"address"},{"internalType":"address","name":"owner","type":"address"}],"name":"ERC2612InvalidSigner","type":"error"},{"inputs":[],"name":"EnforcedPause","type":"error"},{"inputs":[],"name":"ExpectedPause","type":"error"},{"inputs":[],"name":"FailedInnerCall","type":"error"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"currentNonce","type":"uint256"}],"name":"InvalidAccountNonce","type":"error"},{"inputs":[],"name":"InvalidShortString","type":"error"},{"inputs":[],"name":"NotEnoughTreasuryAllowance","type":"error"},{"inputs":[],"name":"OnlyFactory","type":"error"},{"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"SafeERC20FailedOperation","type":"error"},{"inputs":[{"internalType":"string","name":"str","type":"string"}],"name":"StringTooLong","type":"error"},{"inputs":[],"name":"ZeroAddress","type":"error"},{"inputs":[],"name":"ZeroAmount","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[],"name":"EIP712DomainChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Unwrapped","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Wrapped","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"eip712Domain","outputs":[{"internalType":"bytes1","name":"fields","type":"bytes1"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"version","type":"string"},{"internalType":"uint256","name":"chainId","type":"uint256"},{"internalType":"address","name":"verifyingContract","type":"address"},{"internalType":"bytes32","name":"salt","type":"bytes32"},{"internalType":"uint256[]","name":"extensions","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"structHash","type":"bytes32"}],"name":"hashTypedDataV4","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"forwarder","type":"address"}],"name":"isTrustedForwarder","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"permit2","outputs":[{"internalType":"contract IAllowanceTransfer","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"trustedForwarder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"underlyingAsset","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"wrap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"components":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint160","name":"amount","type":"uint160"},{"internalType":"uint48","name":"expiration","type":"uint48"},{"internalType":"uint48","name":"nonce","type":"uint48"}],"internalType":"struct IAllowanceTransfer.PermitDetails","name":"details","type":"tuple"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"sigDeadline","type":"uint256"}],"internalType":"struct IAllowanceTransfer.PermitSingle","name":"permitSingleStruct","type":"tuple"},{"internalType":"bytes","name":"permitSingleSignature","type":"bytes"}],"name":"wrap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"components":[{"components":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint160","name":"amount","type":"uint160"},{"internalType":"uint48","name":"expiration","type":"uint48"},{"internalType":"uint48","name":"nonce","type":"uint48"}],"internalType":"struct IAllowanceTransfer.PermitDetails","name":"details","type":"tuple"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"sigDeadline","type":"uint256"}],"internalType":"struct IAllowanceTransfer.PermitSingle","name":"permitSingleStruct","type":"tuple"},{"internalType":"bytes","name":"permitSingleSignature","type":"bytes"},{"components":[{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"internalType":"struct ITokenPermitSignatureDetails.TokenPermitSignatureDetails","name":"tokenPermitSignatureDetails","type":"tuple"}],"name":"wrap","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
token_contract = web3.eth.contract(address=tokenaddr, abi=tokenabi)
token_contract2 = web3.eth.contract(address=tokenaddr2, abi=tokenabi2)

def txConfirmation(amount, txhash, gasfee, fromtoken, totoken, wpol, tpol):
    try:
        url = f"https://api.tea-fi.com/transaction"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Origin": "https://app.tea-fi.com",
            "Referer": "https://app.tea-fi.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        
        amountwei = web3.to_wei(amount, 'ether')
        
        data = {
            "hash": txhash,
            "blockchainId": 137,
            "type": 2,
            "walletAddress": payer.address,
            "fromTokenAddress": fromtoken,
            "toTokenAddress": totoken,
            "fromTokenSymbol": wpol,
            "toTokenSymbol": tpol,
            "fromAmount": amountwei,
            "toAmount": amountwei,
            "gasFeeTokenAddress": "0x0000000000000000000000000000000000000000",
            "gasFeeTokenSymbol": "POL",
            "gasFeeAmount": gasfee
        }

        response = requests.post(url, headers=headers, json=data)
        return response.json()
    except Exception as e:
        print(f"Error occurred: {e}")

def getGasFee():
    try:
        url = f"https://api.tea-fi.com/transaction/gas-quote?chain=137&txType=2&gasPaymentToken=0x0000000000000000000000000000000000000000&neededGasPermits=0"
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Origin": "https://app.tea-fi.com",
            "Referer": "https://app.tea-fi.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")

def Unwrap(amount):
    try:
        nonce = web3.eth.get_transaction_count(payer.address)
        amountwei = web3.to_wei(amount, 'ether')
        gasAmount = token_contract2.functions.unwrap(amountwei, payer.address).estimate_gas({
            'chainId': chainId,
            'from': payer.address,
            'nonce': nonce
        })
        gasPrice = web3.eth.gas_price
        unwraptx = token_contract2.functions.unwrap(amountwei, payer.address).build_transaction({
            'chainId': chainId,
            'from': payer.address,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        #sign & send the transaction
        print(f'Processing Unwrap {amount} wPOL')
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(unwraptx, payer.key).rawTransaction)
        #wait for transaction
        print(f'Wait For Transaction Until Mined...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        #get transaction hash
        print(f'Processing Unwrap {amount} wPOL Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
        print(f'')
        gasfee = getGasFee()
        if None == gasfee["gasInGasPaymentToken"]:
            print(f'Get Gas Payment Fail!')
        else:
            txconfirm = txConfirmation(amount, str(web3.to_hex(tx_hash)), gasfee["gasInGasPaymentToken"], tokenaddr2, tokenaddr, "tPOL", "WPOL")
            if None == txconfirm["id"]:
                print(f'Transaction Confirmation Fail!')
            else:
                print(f'{txconfirm}')
    except Exception as e:
        print(f"Error: {e}")

def Wrap():
    try:
        nonce = web3.eth.get_transaction_count(payer.address)
        amountwei = web3.to_wei(amount, 'ether')
        gasAmount = token_contract2.functions.wrap(amountwei, payer.address).estimate_gas({
            'chainId': chainId,
            'from': payer.address,
            'nonce': nonce
        })
        gasPrice = web3.eth.gas_price
        wraptx = token_contract2.functions.wrap(amountwei, payer.address).build_transaction({
            'chainId': chainId,
            'from': payer.address,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        #sign & send the transaction
        print(f'Processing Wrap {amount} wPOL')
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(wraptx, payer.key).rawTransaction)
        #wait for transaction
        print(f'Wait For Transaction Until Mined...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        #get transaction hash
        print(f'Processing Wrap {amount} wPOL Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
        print(f'')
        gasfee = getGasFee()
        if None == gasfee["gasInGasPaymentToken"]:
            print(f'Get Gas Payment Fail!')
        else:
            txconfirm = txConfirmation(amount, str(web3.to_hex(tx_hash)), gasfee["gasInGasPaymentToken"], tokenaddr, tokenaddr2, "WPOL", "tPOL")
            if None == txconfirm["id"]:
                print(f'Transaction Confirmation Fail!')
            else:
                print(f'{txconfirm}')
                Unwrap(amount)
    except Exception as e:
        print(f"Error: {e}")
        
def checkApprove():
    try:
        unliappv = 115792089237316195423570985008687907853269984665640564039457584007913129639935
        checkallow = int(token_contract.functions.allowance(payer.address, tokenaddr2).call())
        if checkallow > web3.to_wei(amount, 'ether'):
            print('Already Approve! Processing Wrap wPOL...')
            Wrap()
        else:
            nonce = web3.eth.get_transaction_count(payer.address)
            gasAmount = token_contract.functions.approve(tokenaddr2, unliappv).estimate_gas({
                'chainId': chainId,
                'from': payer.address,
                'nonce': nonce
            })
            gasPrice = web3.eth.gas_price
            appvtx = token_contract.functions.approve(tokenaddr2, unliappv).build_transaction({
                'chainId': chainId,
                'from': payer.address,
                'gas': gasAmount,
                'gasPrice': gasPrice,
                'nonce': nonce
            })
            #sign & send the transaction
            print(f'Processing Approve {amount} wPOL To {tokenaddr2}')
            tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(appvtx, payer.key).rawTransaction)
            #wait for transaction
            print(f'Wait For Transaction Until Mined...')
            transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            #get transaction hash
            print(f'Approve {amount} wPOL To {tokenaddr2} Success!')
            print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
            print(f'')
            Wrap()
    except Exception as e:
        print(f"Error: {e}")
        
for i in range(0,int(loop)):        
    checkApprove()