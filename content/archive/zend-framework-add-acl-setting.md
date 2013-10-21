Title: Zend Framework add Acl setting
Date: 2011-04-24 15:22
Author: carlcarl
Post_ID: 18
Category: Zend Framework
Slug: zend-framework-add-acl-setting

首先先在 `bootstrap.php` 檔案裡加上下面這個 function<!--more-->

	:::php
	<?php
    protected function _initControllers()
	{
		$this->bootstrap('FrontController');
		//require_once '../library/Controller/Helper/Acl.php';
		//require_once '../library/Controller/Plugin/Auth.php';
		$acl = new Controller_Helper_Acl();
		$auth = Zend_Auth::getInstance();
		$front = Zend_Controller_Front::getInstance();
		$front->registerPlugin(new Controller_Plugin_Auth($auth, $acl));
	}


`$acl` 和 `$auth` 這兩個都需要實作，我分別把 `auth` 和 `acl` 這兩個 class 放在 library 底下的 `Controller/Plugin` 和 `Controller/Helper/`。

* * * * *

Acl 裡面實作角色 目錄 權限設定

	:::php
	<?php
	class Controller_Helper_Acl extends Zend_Acl
	{
		public function __construct()
		{
			$this->add(new Zend_Acl_Resource('importstu'));
			$this->add(new Zend_Acl_Resource('coursesetup'));
			$this->add(new Zend_Acl_Resource('homeworksetup'));
			$this->add(new Zend_Acl_Resource('teacher'));
			$this->add(new Zend_Acl_Resource('homework'));
			//$this->add(new Zend_Acl_Resource('Article_Page'));
			$this->add(new Zend_Acl_Resource('index'));
			$this->add(new Zend_Acl_Resource('login'));
			$this->add(new Zend_Acl_Resource('error'));
			$this->addRole(new Zend_Acl_Role('guest'));
			$this->addRole(new Zend_Acl_Role('student'));
			$this->addRole(new Zend_Acl_Role('ta'));
			$this->addRole(new Zend_Acl_Role('teacher'));
			$this->allow('teacher');
			$this->allow('ta', null, null);
			$this->allow('student', null, null);
			$this->deny('student', 'importstu');
			$this->deny('student', 'coursesetup', 'teacher');
			$this->deny('student', 'teacher');
			$this->deny('student', 'homeworksetup');
			$this->deny('guest');
			$this->allow('guest', 'login');
		}
	}


Resource 的名稱我一律用小寫，到時候抓到 controller name 就轉小寫進來判斷，`allow` 和 `deny` 就是讓角色可以進入或禁止進入那些目錄，參數為(角色, controller, action)，`null` 默認為全部, 嫌麻煩的話不寫也是可以。

* * * * *

Auth 是一個 plugin，會抓現在的資料進去 Acl 並作判斷

	:::php
	<?php
	class Controller_Plugin_Auth extends Zend_Controller_Plugin_Abstract
	{
		private $_auth;
		private $_acl;
		public function __construct($auth, $acl)
		{
			$this->_auth = $auth;
			$this->_acl = $acl;
		}
		// 重載 preDispatch() 方法
		public function preDispatch($request)
		{
			parent::preDispatch($request);
			$role = 'guest';
			if (Zend_Auth::getInstance()->hasIdentity())
			{
				$userInfo = $this->getStudentInfo();
				if($userInfo->role == 1)
				{
					$role = 'teacher';
				}
				else if($userInfo->role == 2)
				{
					$role = 'ta';
				}
				else if($userInfo->role == 3)
				{
					$role = 'student';
				}
			}
			else
			{
				$role = 'guest';
			}
			$controller = $request->controller;
			$action = $request->action;
			$module = $request->module;
			$resource = strtolower($controller); //前面提到會轉小寫做判斷
			if (!$this->_acl->has($resource)) //沒加入判斷的controller 預設通過
			{
				$resource = null;
			}
			if (!$this->_acl->isAllowed($role, $resource, $action))
			{
				if (!Zend_Auth::getInstance()->hasIdentity())
				{
					//// 使用者沒登入 就轉登入畫面
					////
				}
				else
				{
					// 用戶沒有目錄的權限 就提示錯誤
					////
				}
			}
			// 設置轉向
			$request->setModuleName($module);
			$request->setControllerName($controller);
			$request->setActionName($action);
		}
	}


設置大概差不多就是這樣。

 

參考網址:  
<http://blogold.chinaunix.net/u2/86974/showart_2219380.html>  
<http://stackoverflow.com/questions/5209671/zend-framework-nedd-typical-example-of-acl>  
<http://codeutopia.net/blog/2009/02/06/zend_acl-part-1-misconceptions-and-simple-acls/>  
