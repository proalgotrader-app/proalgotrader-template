import pandas_ta as ta

from datetime import timedelta

from proalgotrader_protocols import Algorithm_Protocol
from proalgotrader_protocols.enums.account_type import AccountType


class Strategy(Algorithm_Protocol):
    async def initialize(self):
        self.set_account_type(AccountType.DERIVATIVE_INTRADAY)

        self.nifty = self.add_future("NIFTY", ("monthly", 0))

        self.nifty_chart = await self.add_chart(
            self.nifty, timedelta(minutes=5)
        )

    @property
    def sma_20(self):
        return self.nifty_chart.add_indicator(
            "sma_20", lambda data: ta.sma(close=data.close, length=20)
        )

    @property
    def sma_50(self):
        return self.nifty_chart.add_indicator(
            "sma_50", lambda data: ta.sma(close=data.close, length=50)
        )
    
    def crossover(sma1, sma2):
        return True
    
    async def next(self):
        sma_20 = self.sma_20.data["SMA_20"]
        sma_50 = self.sma_50.data["SMA_50"]

        crossover = self.crossover(sma_20, sma_50)

        if crossover:
          if not self.open_positions:
              await self.buy(symbol=self.nifty_ce, quantities=50)
          else:
              await self.buy(symbol=self.nifty_ce, quantities=50)
