steps to setting up a new day
`npm init -y`
`npm install --save-dev typescript`
`npx tsc --init`
`npm install --save-dev @types/node `

Update package.json to read:
```
"scripts": {
  "start": "tsc && node dist/index.js"
}
```


