from pyzil.zilliqa import chain
from flask import Flask, jsonify
import json

app = Flask(__name__)
app.config.from_object(__name__)

def init():
	chain.set_active_chain(chain.MainNet)

@app.route('/addressState/<address>, 'methods=['GET'])
def get_contract_state(address):
	chain.active_chain.api.GetSmartContractState(address)


if __name__ == '__main__':
	# address = "fe001824823b12b58708bf24edd94d8b5e1cfcf7"
    app.run()
