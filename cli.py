import typer
from client import BinanceFuturesClient
from logger import setup_logger


setup_logger()


client = BinanceFuturesClient()


def main(
    symbol: str = typer.Option(...),
    side: str = typer.Option(...),
    order_type: str = typer.Option(...),
    quantity: float = typer.Option(...),
    price: float = typer.Option(None),
    leverage: int= typer.Option(10), 
    stop_loss: float = typer.Option(None),
    take_profit: float = typer.Option(None)
):
    try:
        client = BinanceFuturesClient()

        side = side.upper()
        order_type = order_type.upper()

    

        print("\n--- Order Request ---")
        print(symbol, side, order_type, quantity, price)

        response = client.place_order(symbol, side, order_type, quantity, price, leverage, stop_loss, take_profit)

        print("\n--- Response ---")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

        print("\n Success")

    except Exception as e:
        print(f"\n Error: {e}")

if __name__ == "__main__":
    typer.run(main)