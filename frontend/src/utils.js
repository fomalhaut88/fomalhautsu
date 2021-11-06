function haveIntersection(arr1, arr2) {
  return !!arr1.filter(e => arr2.includes(e)).length
}

function inlineUpmathToMathjax(s) {
  s = s.replace(/\$\$/g, '$')
  s = s.replace(/<p>\$(.*?)\$<\/p>/g, '<p class="text-center">$$ $1 $$</p>')
  return s
}

function removeUpmathSpecs(s) {
  s = s.replace(/\$\$/g, '')
  s = s.replace(/##+/g, '')
  return s
}

function emailIsValid(s) {
  return s.match(/^[a-zA-Z0-9\-_.]+?@[a-zA-Z0-9\-_.]+?\.[a-zA-Z0-9\-_]+?$/)
}

function toCebabCase(s) {
  return strip(
    s.replace(/\W+/g, '-').toLowerCase(),
    '-'
  )
}

function strip(s, c) {
  let i = 0
  let j = s.length
  while ((i < j) && (s[i] == c)) {
    i++
  }
  while ((i < j) && (s[j - 1] == c)) {
    j--
  }
  return s.substring(i, j)
}

export {
  haveIntersection,
  inlineUpmathToMathjax,
  removeUpmathSpecs,
  emailIsValid,
  toCebabCase,
  strip,
}
