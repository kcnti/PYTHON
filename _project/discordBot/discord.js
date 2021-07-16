const { exec } = require('child_process');
const fs = require("fs");
const Discord = require("discord.js");

let client = new Discord.Client();
client.config = JSON.parse(fs.readFileSync("config.json", "utf8"));
const options = {
	split: {
		char: "\n",
		prepend: "```",
		append: "```"
	}
}

client.on("message", msg => {
	
	if (msg.content == ".clear"){
		messages = msg.channel.fetchMessages()
			.then(function(list){
				message.channel.bulkDelete(list);
			})
	}
//	if(!msg.member.roles.cache.some(role => role.name === "spam permission")) return msg.channel.send("FUCK OFF EIEI")
//		break;
	if (msg.channel.id === client.config.channel && msg.member.roles.cache.some(role => role.name === "spam permission")) exec(msg.content, (err, stdout, stderr) => {
//  	msg
		if (err) console.error(err);
//		if (stdout) msg.channel.send("```\n" + Discord.escapeMarkdown(stdout, true) + "```", options);
//		if (stderr) msg.channel.send("```\n" + Discord.escapeMarkdown(stderr, true) + "```", options);
	});
	else {
	msg.reply("FUCK OFF EIEI")
}
	
});

client.on("ready", () => console.log(`Logged in as ${client.user.tag}`));

client.login(client.config.token);
