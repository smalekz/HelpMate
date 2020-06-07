# HelpMate BlockChain-based deal managment

from easy_blockchain.wallet import Wallet
from easy_blockchain.blockchain import Block, BlockChain

# Create the first user
helpmate = Wallet()
user01 = helpmate.getPublicKey()
trans01 = helpmate.create_transaction('test01', 1, 0.5, 'one message')
trans02 = trans01.copy() # create a forgery attack
print('Check if a forgery attack have same as real transaction')
print('trans01 == trans02', trans01 == trans02)

# Create the second user
helpmate2 = Wallet()
user02 = helpmate2.getPublicKey()
trans03 = helpmate2.create_transaction(user01, 1.5, 0.12,'user02 send to user01')

block = Block()
block.add_transaction(trans01)
block.add_transaction(trans02)  # check adding a forgery attack
block.add_transaction(trans03)

# check how many transactions were added
print('--------------------------------------')
print('The block 1 have 2 real transaction:')
print(json.dumps(block.transactions, indent=2))
# create a blockchain and become an miner
deal = BlockChain()
# mine a proof
proof = deal.mine_proof()
print('The first proof is:',proof)
# save blockchain to local database
deal.save_chain()

print('--------------------------------------')
print('The transaction history and the balance of users:')
mydeal = deal.get_history(user01)
print('User: user01 balance:', deal.get_balance(user01))
print(json.dumps(mydeal, indent=4))

mydeal = deal.get_history(user02)
print('User: user02 balance:', deal.get_balance(user02))
print(json.dumps(mydeal, indent=4))

mydeal = deal.get_history(user03)
print('User: user03 balance:', deal.get_balance(user03))
print(json.dumps(mydeal, indent=4))
