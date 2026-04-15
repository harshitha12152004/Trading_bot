from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging
from config import API_KEY, API_SECRET

class BinanceFuturesClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None, leverage=10, stop_loss=None, take_profit=None):
        try:
            self.client.futures_change_leverage(symbol=symbol, leverage=leverage)
            logging.info(f"Placing order: {symbol}, {side}, {order_type}, {quantity}, {price} lev={leverage}")

            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            order = self.client.futures_create_order(**params)
            if stop_loss:
                self.client.futures_create_order(
                       symbol=symbol,
                       side="SELL" if side == "BUY" else "BUY",
                       type="STOP_MARKET",
                       stopPrice=stop_loss,
                       closePosition=True
                )


            if take_profit:
               self.client.futures_create_order(
                   symbol=symbol,
                   side="SELL" if side == "BUY" else "BUY",
                   type="TAKE_PROFIT_MARKET",
                   stopPrice=take_profit,
                   closePosition=True
                )

            return order

        except Exception as e:
            logging.error(f"Error: {e}")
            raise

            