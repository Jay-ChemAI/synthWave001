const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3001;

app.get('/Bot1', (req, res) => {
  const cmd = 'rcc run';
  const botDir = 'C:\\Users\\javie\\OneDrive\\Escritorio\\synthWave1\\synthwave001\\bots\\CMS_Provider_data';
  exec(`cd ${botDir} && ${cmd}`, (error, stdout, stderr) => {
    if (error) {
      console.log(`error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.log(`stderr: ${stderr}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    res.send(stdout);
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
