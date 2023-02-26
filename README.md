# ft_2_rm
sync pdf copies of FT tech news to remarkable2, using 12ft.io to avoid paywall

you can alter the ft url if you want different news content

will work until ft change their page markup :)


## dependencies
1. python libs

```$ pip install -r requirements.txt```

2. wkhtmltopdf, required by pdfkit

debian

```$ sudo apt-get install wkhtmltopdf```

macos

```$ brew install homebrew/cask/wkhtmltopdf```

3. chrome

yes, it uses chrome headless to produce the pdf documents, you could use chromium if you are a free software fan :)

4. rmapi
> rMAPI is a Go app that allows you to access the ReMarkable Cloud API programmatically.
https://github.com/juruen/rmapi/blob/master/README.md

something like this will get you up and running

```go get -u github.com/juruen/rmapi```

once installed just run `rmapi` to set up authentication
