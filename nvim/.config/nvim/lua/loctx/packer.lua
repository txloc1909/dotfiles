local ensure_packer = function()
	local fn = vim.fn
	local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
	if fn.empty(fn.glob(install_path)) > 0 then
		fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
		vim.cmd [[packadd packer.nvim]]
		return true
	end
	return false
end

local packer_bootstrap = ensure_packer()

vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
	-- Packer can manage itself
	use 'wbthomason/packer.nvim'

	use {
		'nvim-telescope/telescope.nvim', tag = '0.1.0',
		requires = { {'nvim-lua/plenary.nvim'} }
	}

	use {
		'NLKNguyen/papercolor-theme',
		config = function()
			vim.cmd("set background=dark")
			vim.cmd("colorscheme PaperColor")
		end,
	}

	use {
		'nvim-treesitter/nvim-treesitter',
		run = ':TSUpdate'
	}

	use { 'theprimeagen/harpoon' }

	use { 'mbbill/undotree' }

	use { 'tpope/vim-fugitive' }
	use { 'tpope/vim-commentary' }
	use { 'tpope/vim-rsi' }

	use {
		'VonHeikemen/lsp-zero.nvim',
		branch = 'v1.x',
		requires = {
			-- LSP Support
			{'neovim/nvim-lspconfig'},             -- Required
			{'williamboman/mason.nvim'},           -- Optional
			{'williamboman/mason-lspconfig.nvim'}, -- Optional

			-- Autocompletion
			{'hrsh7th/nvim-cmp'},         -- Required
			{'hrsh7th/cmp-nvim-lsp'},     -- Required
			{'hrsh7th/cmp-buffer'},       -- Optional
			{'hrsh7th/cmp-path'},         -- Optional
			{'saadparwaiz1/cmp_luasnip'}, -- Optional
			{'hrsh7th/cmp-nvim-lua'},     -- Optional

			-- Snippets
			{'L3MON4D3/LuaSnip'},             -- Required
			{'rafamadriz/friendly-snippets'}, -- Optional
		}
	}

	use { 'mhinz/vim-sayonara' }
	use {
		'windwp/nvim-autopairs',
		config = function()
			require('nvim-autopairs').setup({
				enable_check_bracket_line = false,
				map_cr = true,
			})
		end,
	}

	use {
		'kylechui/nvim-surround',
		config = function()
			require('nvim-surround').setup({})
		end,
	}

	use {
		'mhinz/vim-signify',
		config = function()
			vim.g.signify_disable_by_default = false
		end,
	}

	use {
		'shortcuts/no-neck-pain.nvim',
		tag = '*',
		config = function()
			require('no-neck-pain').setup({ width = 120, })
		end,
	}
end)
