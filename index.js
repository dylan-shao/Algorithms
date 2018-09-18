const fs = require('fs');
const header =
  '## Algorithms\n' +
  'This is a Algorithms Practice Repo to help me understanding data structures.\n' +
  'All algorithms are written in Java, JavaScript and Python.' +
  '\n' +
  '\n' +
  '----------' +
  '\n' +
  '\n' +
  '|Algorithm|  Java           | Python  |  JavaScript\n' +
  '|--- |:--------------:| :-------:|  :---:\n';

fs.writeFileSync('README.md', header);
console.log('write header done!');

let javaFiles = 0;
let pyFiles = 0;
let jsFiles = 0;

function getUrl(
  path,
  repoName = 'test_watch_files_create_readme',
  branchName = 'master',
) {
  return `https://github.com/dylan-shao/${repoName}/blob/${branchName}/${path}`;
}

(function f(dir) {
  fs.readdir(dir, (err, files) => {
    for (let i = 0; i < files.length; i++) {
      const file = files[i];

      // ignore unwanted files or folders
      if (
        !/^(node_modules)|^package.*$|^index\.js.*$|^README\.md.*$|((^|[\/\\])\..)/.test(
          file,
        )
      ) {
        const fileOrFolderName = dir + '/' + file;

        /*---------------------if is directory-------------------*/
        if (fs.statSync(fileOrFolderName).isDirectory()) {
          const folderName = fileOrFolderName.replace('./', '');
          if (folderName.indexOf('/') < 0 && folderName.indexOf('.') < 0) {
            const content = `|**${folderName}**|*********|*********|*********\n`;
            fs.appendFile('README.md', content, function(err) {
              if (err) throw err;
              console.log('Saved!');
            });
          }
          f(fileOrFolderName);
          /*-------------------------------------------------------*/
        } else {
          /*---------------------if is file----------------------*/
          const defaultName = 'Todo...';
          let javaName = defaultName;
          let javaPath;
          let pyName = defaultName;
          let pyPath;
          let jsName = defaultName;
          let jsPath;
          // if this is file, get parent folder, check all files at once and save them into one line content
          const files = fs.readdirSync(dir);
          files.forEach(file => {
            console.log('######', file);
            const fileName = (dir + '/' + file).replace('./', '');
            if (file.indexOf('.java') >= 0) {
              javaFiles++;
              javaName = file;
              javaPath = getUrl(fileName);
            } else if (file.indexOf('.py') >= 0) {
              pyFiles++;
              pyName = file;
              pyPath = getUrl(fileName);
            } else if (file.indexOf('.js') >= 0) {
              jsFiles++;
              jsName = file;
              jsPath = getUrl(fileName);
            }
          });
          const content = `|| [${javaName}](${javaPath})|[${pyName}](${pyPath})|[${jsName}](${jsPath})\n`;
          fs.appendFile('README.md', content, function(err) {
            if (err) throw err;
            console.log('Saved!');
          });

          // if is file, break out of the loop, because we already jumped out to the parent and appended the content above
          break;
          /*----------------------------------------------------*/
        }
      }
    }
    console.log(javaFiles, pyFiles, jsFiles);
  });
})('.');