
# Hyperpub :thought_balloon:

Tired of using LaTex? Want to write Lit. Prog. python in Vim (or your editor of
choice)? Want to be able to style your documents with CSS? Me too.

That's why i wrote this package, that lets you make nice-looking documents. It
even lets you put plots and tables right into the doc!

Usage:

``````
```{my block}
df = pd.DataFrame([[1,2,3],[4,5,6]])
rndrtable(df)
```
``````

This outputs the table as HTML in your markdown.

Also works with plots:

``````
```{my plot}
plt.plot([1,2,3],[3,4,5])
rndrplot()
```
``````

To render, use `hyperpub [infile] [outfile]`.

Enjoy!
