# Brokerage, communities and attack fragility

> **Provenance and scope.** Coursework portfolio reconstruction, 2026. Included: participation and connectivity helpers plus tests on small known graphs. The original weighted edge list, null simulations and assessed report are not included, so the reported 77-node experiment cannot be rerun here.

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


## Licence

Original material is available for portfolio evaluation under the [evaluation-only licence](LICENSE). Third-party data, libraries and original assessment materials retain their own terms.
