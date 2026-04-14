Crypto Trader Behavior Analysis: Fear vs. Greed
1. Methodology
Data Preparation & Alignment:

Trades Dataset: 211,224 rows processed. Formatted timestamps to IST daily level. Cleaned direction flags to map specific actions to binary Is_Long or Is_Short variables. Filtered win rates exclusively on closed trades (where PnL != 0).

FGI Dataset: 2,644 rows processed. Simplified the 0-100 index into three macro-regimes: Fear (0-45), Neutral (46-54), and Greed (55-100).

Alignment: Both datasets were merged using an inner join on the standard Date key.

Feature Engineering: Derived metrics including Win Rate, Average Trade Size (USD), Long/Short Ratio, and Daily Trade Frequency. Grouped accounts by historical activity to create behavioral segments (Frequent vs. Infrequent; High Volume vs. Low Volume). (Note: Leverage distribution was omitted as the provided dataset lacked margin/collateral fields).

2. Key Insights
Profitability Scales with Fear: While the overall win rate drops during Fear regimes (50.5% vs 55.1% in Greed), the average realized PnL per trade nearly doubles ($272.24 in Fear vs. $140.71 in Greed). Volatility creates larger payout tails.

Hyperactivity in Panicky Markets: Fear markets trigger immense volume spikes. Traders executed an average of 5,327 trades/day during Fear, compared to just 1,119 trades/day during Greed. Furthermore, the average trade size swelled by ~56% ($7,150 vs $4,580) when the market was fearful.

Behavioral Divergence by Segment: "Frequent" (highly active) traders dominated Fear markets, capturing over $3.43M in aggregate PnL while swinging massive sizes. Conversely, "Infrequent" (retail-style) traders underperformed in Fear but saw their PnL explode to over $1.52M during steady Greed conditions.

Directional Bias: Greed markets exhibit neutral positioning (Long/Short ratio of 0.97). Fear markets trigger heavy short-selling behavior (Long/Short ratio plunges to 0.58).

3. Strategy Recommendations (Rules of Thumb)
Based on the behavioral archetypes and market sentiment regimes, I propose the following data-backed strategies:

Rule 1: The "Volatility Harvesting" Protocol (For Frequent/Algorithmic Traders)

Trigger: FGI drops into 'Fear'.

Action: Increase position sizing and strictly adopt a Short-bias (following the 0.58 L/S flow). Do not optimize for Win Rate; optimize for payout size. The data shows that while win rates dip in Fear, the average successful PnL roughly doubles. Capitalize on the wider tail-ends of price swings.

Rule 2: The "Trend-Ride" Protocol (For Infrequent/Retail Traders)

Trigger: FGI drops into 'Fear'.

Action: Reduce trade frequency and scale down capital deployed. Infrequent traders get "chopped up" during high-volatility panics. Move to the sidelines to conserve cash, and aggressively scale into Long setups only once sentiment rotates back to 'Greed', where this segment's aggregate profitability is historically 2.5x higher.