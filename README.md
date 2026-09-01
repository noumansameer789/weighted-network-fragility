# Brokerage, communities and attack fragility

Weighted-network analysis separating popularity, brokerage, cross-community
participation and attack consequence instead of treating them as one concept.

## Reported result from the original experiment

- 77 nodes, 254 weighted edges and six Louvain communities
- 200 degree-preserving null graphs
- observed clustering: 17.8 SD above the null mean
- weighted modularity: 12.4 SD above the null mean (`p < 0.005`)
- removing the top 10% by betweenness left 44.2% in the largest component,
  versus 85.9% under random loss averaged over 500 runs

## Executable portfolio layer

The dependency-light module calculates cross-community participation and the
largest-component fraction after node removal. Unit tests verify the attack
consequence on a known graph. The original weighted edge list is not committed.

```bash
python -m unittest discover -s tests -v
```
