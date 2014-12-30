Rails.application.routes.draw do
  resources :visits, only: [:index, :create]

  root 'welcome#index'
end
