# Theme for blog.data.gouv.fr

Forked from [pelican-bootstrap3 theme](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3)

## Working on templates

For instructions and details on Pelican theming,
see [the dedicated section in the documentation](http://docs.getpelican.com/en/3.7.1/themes.html)

## Working on assets (style, script)

Install dependencies using `npm` or `yarn`

```shell
yarn
```

Build with:

```shell
npm run build
```

This will process sources file from `src` directory to the `static` directory:

- minify the JavaScript
- compile and minify the sass/sccs style
- optimize images
- copy fonts

To watch changes and continuously build:

```shell
npm run watch
```
