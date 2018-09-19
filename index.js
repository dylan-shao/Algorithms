/*
* DO-NOT-REPEAT-MYSELF series: https://github.com/dylan-shao/DO-NOT-REPEAT-MYSELF
*
* This file will iterate the folders in this repo, and automatically generate a README.md
* with Links and file name in there, when commit the code.
* Click the repo name on top to see what the README.md looks like!
*/

const fs = require('fs');

const fileName = 'README.md';
const summary =
  'Totally {{javaFiles}} Java files, {{pyFiles}} Python files, {{jsFiles}} JavaScript files';
const header =
  '> This README.md is created automatically when commit the code, used [`pre-commit`](https://www.npmjs.com/package/pre-commit) to hook up [this script to create a README.md by iterating the folders using the `nodejs` `fs` module](https://github.com/dylan-shao/Algorithms/blob/master/index.js). \n' +
  '## Algorithms\n' +
  'This is a Algorithms Practice Repo to help me understanding data structures.\n' +
  'All algorithms are written in Java, JavaScript and Python.' +
  '\n' +
  '\n' +
  '----------' +
  '\n' +
  '\n' +
  summary +
  '\n' +
  '\n' +
  '|Algorithm|  Java  | Python  |  JavaScript\n' +
  '|--- |:--------------:| :-------:|  :---:\n';

fs.writeFileSync(fileName, header);

let javaFiles = 0;
let pyFiles = 0;
let jsFiles = 0;
const emojiForFolder = ':seedling::seedling::seedling:';
const emojiForSeperation = ':wavy_dash::wavy_dash::wavy_dash::wavy_dash:';
const defaultName = 'Todo...';

(function f(dir) {
  const filesOrFolders = fs.readdirSync(dir);
  for (let i = 0; i < filesOrFolders.length; i++) {
    const fileOrFolder = filesOrFolders[i];

    // ignore unwanted files or folders
    if (
      !/^(node_modules)|^package.*$|^index\.js.*$|^README\.md.*$|((^|[\/\\])\..)/.test(fileOrFolder)
    ) {
      const fileOrFolderName = dir + '/' + fileOrFolder;

      /*---------------------if is directory-------------------*/
      if (fs.statSync(fileOrFolderName).isDirectory()) {
        // fileOrFolderName start with ./path/to...., so remove it
        const folderName = fileOrFolderName.replace('./', '');

        // only if it's the 1st layer folder, then we create a row with folder name and * in there
        if (folderName.indexOf('/') < 0 && folderName.indexOf('.') < 0) {
          const content = `|${emojiForFolder}**${folderName}**${emojiForFolder}|${emojiForSeperation}|${emojiForSeperation}|${emojiForSeperation}\n`;
          _append(content);
        }

        //Recursion
        f(fileOrFolderName);
        /*-------------------------------------------------------*/
      } else {
        /*---------------------if is file----------------------*/
        // get parent folder, check all files at once and save them into one line content
        const files = fs.readdirSync(dir);
        const contents = { java: [], py: [], js: [] };

        files.forEach(file => {
          const filePath = (encodeURIComponent(dir) + '/' + file).replace('./', '');

          const name = file;
          const path = _getUrl(filePath);

          if (file.indexOf('.java') >= 0) {
            javaFiles++;
            contents.java.push({ name, path });
          } else if (file.indexOf('.py') >= 0) {
            pyFiles++;
            contents.py.push({ name, path });
          } else if (file.indexOf('.js') >= 0) {
            jsFiles++;
            contents.js.push({ name, path });
          }
        });
        const questionName = '*' + `${dir.substr(dir.lastIndexOf('/') + 1)}` + '*';
        const content =
          `|${questionName}` +
          `|${_getCellContent(contents.java)}` +
          `|${_getCellContent(contents.py)}` +
          `|${_getCellContent(contents.js)}\n`;

        _append(content);

        // if is file, break out of the loop, because we already jumped out to the parent and appended the content above
        break;
        /*----------------------------------------------------*/
      }
    }
  }
})('.');

/*---------------------------replace placeholders---------------------------*/
const data = fs.readFileSync(fileName).toString();

const replaceMap = {
  '{{javaFiles}}': javaFiles,
  '{{pyFiles}}': pyFiles,
  '{{jsFiles}}': jsFiles
};
fs.writeFileSync(fileName, _parseString(data, replaceMap), function(err) {
  if (err) throw err;
});

console.log(_parseString(summary, replaceMap));

/*------------------------------Utilities-------------------------------------*/
function _getUrl(path, repoName = 'Algorithms', branchName = 'master') {
  return `https://github.com/dylan-shao/${repoName}/blob/${branchName}/${path}`;
}

function _append(content) {
  fs.appendFile(fileName, content, function(err) {
    if (err) throw err;
  });
}

// arg: [{name:'', path:''},...]
function _getCellContent(arr) {
  if (!arr.length) {
    return defaultName;
  }
  let res = '';
  arr.forEach(({ name, path }) => {
    res += `[${name}](${path})<br>`;
  });
  return res;
}

// const summary = `\nTotally ${javaFiles} Java files, ${pyFiles} Python files, ${jsFiles} JavaScript files\n`;
// replace string with values defined in the mapObj, whose key is the string you want to replace, and value is the value
function _parseString(str, mapObj) {
  var re = new RegExp(Object.keys(mapObj).join('|'), 'gi');

  return str.replace(re, function(matched) {
    return mapObj[matched];
  });
}
