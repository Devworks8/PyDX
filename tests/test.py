from PyDX import pydx

nested = {"Settings":
              {"General":
                   {"Font":
                        {"Name": "Helvica",
                         "Size": "1"
                         }
                    },
               "Network":
                   {"Frontend":
                        {"ip": "127.0.0.1",
                         "port": "6000"},
                    "Backend":
                        {"ip": "127.0.0.1",
                         "port": "6001"
                         }
                    }
               }
          }

expected_results = {'Settings_General_Font_Name': 'Helvica',
                    'Settings_General_Font_Size': '1',
                    'Settings_Network_Frontend_ip': '127.0.0.1',
                    'Settings_Network_Frontend_port': '6000',
                    'Settings_Network_Backend_ip': '127.0.0.1',
                    'Settings_Network_Backend_port': '6001'}

flat = pydx.flatten(nested)
assert expected_results == flat

expand = pydx.inflate(flat)
assert nested == expand
