import React from "react";
import Web3 from "web3";
import axios from "axios";
import * as settings from "../../settings";

export default async function CheckWeb3(props) {
  // Modern dapp browsers...
  var web3 = new Web3();
  if (window.ethereum) {
    window.web3 = new Web3(window.ethereum);
    try {
      // Request account access if needed
      await window.ethereum.enable();
      // Acccounts now exposed
      // web3.eth.sendTransaction({/* ... */});
    } catch (error) {
      // User denied account access...
      console.log(error);
    }
  }
  // Legacy dapp browsers...
  else if (window.web3) {
    window.web3 = new Web3(web3.currentProvider);
    // Acccounts always exposed
    // web3.eth.sendTransaction({/* ... */});
  }
  window.ethereum.enable();

  if (typeof web3 != "undefined") {
    // console.log(window.web3.currentProvider);
    window.ethereum.enable();
  }
  // else {
  //   this.web3Provider = new Web3.providers.WebsocketProvider(
  //     settings.INFURA_WEBSOCKET_API
  //   );
  //   window.ethereum.enable();
  // }

  var address = window.ethereum.selectedAddress;

  // axios
  //   .post(`${settings.API_SERVER}/api/app/tokenuri/`, {
  //     address: address,
  //   })
  //   .then((res) => {
  //     console.log(res);
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });

  return address;
}
