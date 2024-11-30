// Define los parámetros de la red personalizada.
const networkData = {
    chainId: '0x45c', // Cambia esto por el ID de la cadena que quieras agregar (en hexadecimal).
    chainName: 'Core Blockchain Mainnet', // Nombre de la red.
    nativeCurrency: {
      name: 'CORE', // Nombre de la moneda.
      symbol: 'CORE', // Símbolo.
      decimals: 18, // Decimales.
    },
    rpcUrls: ['https://core.drpc.org/'], // URL RPC de la red.
    blockExplorerUrls: ['https://scan.coredao.org/'], // URL del explorador.
  };
  
  // Asocia un evento al botón.
  document.getElementById('add-network-button').addEventListener('click', async () => {
    try {
      if (window.ethereum) {
        // Llama al método de MetaMask para agregar la red.
        await window.ethereum.request({
          method: 'wallet_addEthereumChain',
          params: [networkData],
        });
      }
    } catch (error) {
      console.error('Error al agregar la red:', error);
    }
  });
  