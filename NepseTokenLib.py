import requests

class TokenParser():
    def __init__(self):
        ###############################################MAGIC ARRAY###############################################
        #FOR details check http://newweb.nepalstock.com/assets/prod/css.wasm
        #decompiling the wasm gives access to the following magic array and (rdx, cdx) function
        self.data_segment_data_0 = [
                                      0x09, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 
                                      0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 
                                      0x02, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 
                                      0x07, 0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 
                                      0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
                                      0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 
                                      0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
                                      0x09, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 
                                      0x06, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x07, 0x00, 0x00, 0x00, 
                                      0x02, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x06, 0x00, 0x00, 0x00, 
                                      0x09, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 
                                      0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 
                                      0x03, 0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 
                                      0x04, 
                                    ]
        
    def rdx(self, w2c_p0, w2c_p1, w2c_p2, w2c_p3, w2c_p4):

        w2c_i0 = w2c_p1
        w2c_i1 = 100
        w2c_i0 = w2c_i0 // w2c_i1
        w2c_i1 = 10
        w2c_i0 = w2c_i0 % w2c_i1
        w2c_i1 = w2c_p1
        w2c_i2 = 10
        w2c_i1 = w2c_i1 // w2c_i2
        w2c_p0 = w2c_i1
        w2c_i2 = 10
        w2c_i1 = w2c_i1 % w2c_i2
        w2c_i0 += w2c_i1
        w2c_p2 = w2c_i0
        w2c_i1 = w2c_p2
        w2c_i2 = w2c_p1
        w2c_i3 = w2c_p0
        w2c_i4 = 10
        w2c_i3 *= w2c_i4
        w2c_i2 -= w2c_i3
        w2c_i1 += w2c_i2
        w2c_i2 = 2
        w2c_i1 <<= (w2c_i2 & 31)

        w2c_i1 = self.data_segment_data_0[w2c_i1]
        w2c_i0 += w2c_i1
        w2c_i1 = 22
        w2c_i0 += w2c_i1
        return w2c_i0


    def cdx(self, w2c_p0, w2c_p1, w2c_p2, w2c_p3, w2c_p4):
        w2c_i0 = w2c_p1
        w2c_i1 = 10
        w2c_i0 = w2c_i0 // w2c_i1
        w2c_p0 = w2c_i0
        w2c_i1 = 10
        w2c_i0 = w2c_i0 % w2c_i1
        w2c_i1 = w2c_p1
        w2c_i2 = w2c_p0
        w2c_i3 = 10
        w2c_i2 *= w2c_i3
        w2c_i1 -= w2c_i2
        w2c_i0 += w2c_i1
        w2c_i1 = w2c_p1
        w2c_i2 = 100
        w2c_i1 = w2c_i1 // w2c_i2
        w2c_i2 = 10
        w2c_i1 = w2c_i1 % w2c_i2
        w2c_i0 += w2c_i1
        w2c_i1 = 2
        w2c_i0 <<= (w2c_i1 & 31)

        w2c_i0 = self.data_segment_data_0[w2c_i0]
        w2c_i1 = 22
        w2c_i0 += w2c_i1

        return w2c_i0

    def parse_token_response(self, token_response):
        n = self.cdx(token_response['salt1'], token_response['salt2'], token_response['salt3'], token_response['salt4'], token_response['salt5']);
        l = self.rdx(token_response['salt1'], token_response['salt2'], token_response['salt4'], token_response['salt3'], token_response['salt5']);
        
        i = self.cdx(token_response['salt2'], token_response['salt1'], token_response['salt3'], token_response['salt5'], token_response['salt4']);
        r = self.rdx(token_response['salt2'], token_response['salt1'], token_response['salt3'], token_response['salt4'], token_response['salt5']);

        access_token  = token_response['accessToken']
        refresh_token = token_response['refreshToken']
        
        parsed_access_token  = access_token[0:n] + access_token[n + 1: l] + access_token[l + 1:]
        parsed_refresh_token = refresh_token[0:i] + refresh_token[i + 1: r] + refresh_token[r + 1:]
    
        #returns both access_token and refresh_token, i don't know what's the purpose of refresh token.
        #Right now new access_token can be used for every new api request
        return { 'accessToken': parsed_access_token, 'serverTime': token_response['serverTime'] }

class NepseToken:
    def __init__(self):
        self.token_request_count = 0 
        
        self.token_parser     = TokenParser()

        self.base_url             = "https://www.nepalstock.com.np"
        
        self.token_url            = f"{self.base_url}/api/authenticate/prove"
    
        self.headers= {
                            #host doesn't work with https prefix so removing it
                            'Host': self.base_url.replace('https://', ''),
                            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
                            'Accept': 'application/json, text/plain, */*',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Connection': 'keep-alive',
                            'Referer': f'{self.base_url}',
                            'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache',
                            'TE': 'Trailers',
                        }
    ###############################################PRIVATE METHODS###############################################
    
    def requestToken(self, url):    
        response = requests.get(url, headers=self.headers)
        if (response.status_code != 200):
            return self.requestToken(url)
        else:
            return response.json()

    def incrementTokenRequestCount(self):
        self.token_request_count += 1    
    
    ########################################################PUBLIC METHODS######################################################
    def getValidToken(self):
        self.incrementTokenRequestCount()
        token_response = self.requestToken(url=self.token_url)  
        return self.token_parser.parse_token_response(token_response)

def test():
    nepse_token = NepseToken()
    print(nepse_token.getValidToken())

if __name__ == '__main__':
    test()